#!/usr/bin/env python3

import json
import os
from typing import Dict, List, Any

class ReflectionAgentTest:
    def __init__(self, tree_file: str):
        with open(tree_file, 'r') as f:
            self.tree_data = json.load(f)
        
        self.nodes = {node['id']: node for node in self.tree_data['nodes']}
        
        self.state = {
            'answers': {},
            'path': [],
            'axis1': {'internal': 0, 'external': 0},
            'axis2': {'contribution': 0, 'entitlement': 0},
            'axis3': {'self': 0, 'other': 0}
        }
        
        self.signals_mapping = {
            'axis1:internal': ('axis1', 'internal'),
            'axis1:external': ('axis1', 'external'),
            'axis2:contribution': ('axis2', 'contribution'),
            'axis2:entitlement': ('axis2', 'entitlement'),
            'axis3:self': ('axis3', 'self'),
            'axis3:other': ('axis3', 'other'),
        }
    
    def get_node(self, node_id: str) -> Dict[str, Any]:
        return self.nodes.get(node_id)
    
    def find_child(self, parent_id: str, child_type: str = None) -> Dict[str, Any]:
        """Find a child node by parentId, optionally filtering by type."""
        for node in self.tree_data['nodes']:
            if node.get('parentId') == parent_id:
                if child_type is None or node.get('type') == child_type:
                    return node
        return None
    
    def record_signal(self, signal: str):
        if signal in self.signals_mapping:
            axis, pole = self.signals_mapping[signal]
            self.state[axis][pole] += 1
            print(f"    [Signal recorded: {signal}]")
    
    def interpolate_text(self, text: str) -> str:
        """Replace {NODE_ID.answer} with actual answers from state"""
        for node_id, answer in self.state['answers'].items():
            placeholder = f"{{{node_id}.answer}}"
            text = text.replace(placeholder, answer)
        return text
    
    def route_decision(self, rules_str: str, selected_option: int) -> str:
        """Parse decision rules: answer=A:NODE1;answer=B:NODE2;..."""
        option_letter = chr(65 + selected_option)  # A, B, C, D...
        
        for rule in rules_str.split(';'):
            if f"answer={option_letter}:" in rule:
                return rule.split(':', 1)[1].strip()
        return None
    
    def walk_tree(self, node_id: str = 'START', auto_choices: List[int] = None, choice_index: int = 0):
        """Recursively walk the tree with auto-selection"""
        if not node_id:
            return choice_index
        
        node = self.get_node(node_id)
        if not node:
            print(f"[Error: Node {node_id} not found]")
            return choice_index
        
        self.state['path'].append(node_id)
        
        node_type = node['type']
        text = self.interpolate_text(node['text'])
        
        # Record signal
        if node.get('signal'):
            self.record_signal(node['signal'])
        
        # Handle each node type
        if node_type in ['start', 'bridge']:
            print(f"\n{text}\n")
            if node.get('target'):
                choice_index = self.walk_tree(node['target'], auto_choices, choice_index)
        
        elif node_type == 'question':
            print(f"\n{text}\n")
            options = node['options']
            for i, opt in enumerate(options, 1):
                print(f"{i}. {opt}")
            
            # Auto-select
            if auto_choices and choice_index < len(auto_choices):
                choice = auto_choices[choice_index]
                choice_index += 1
            else:
                choice = 0  # Default to first if not enough choices
            
            print(f"\n[AUTO-SELECTED: {choice + 1}]\n")
            
            # Store the answer
            self.state['answers'][node_id] = options[choice].split(') ')[0].strip()
            
            # Route through decision node using target or parentId lookup
            decision_node_id = node.get('target')
            decision_node = None
            if decision_node_id:
                decision_node = self.get_node(decision_node_id)
            else:
                # Fallback: find the decision node that is a child of this question
                decision_node = self.find_child(node_id, 'decision')
            
            if decision_node:
                next_id = self.route_decision(decision_node['options'], choice)
                if next_id:
                    choice_index = self.walk_tree(next_id, auto_choices, choice_index)
                else:
                    print(f"[Error: No matching route in decision for choice {choice}]")
            else:
                print(f"[Error: No decision node found for {node_id}]")
        
        elif node_type == 'reflection':
            print(f"\n>> {text}\n")
            if node.get('target'):
                choice_index = self.walk_tree(node['target'], auto_choices, choice_index)
        
        elif node_type == 'summary':
            print(f"\n{'='*70}")
            print("YOUR REFLECTION SUMMARY")
            print(f"{'='*70}\n")
            print(text)
            print(f"\n{'='*70}\n")
            if node.get('target'):
                choice_index = self.walk_tree(node['target'], auto_choices, choice_index)
        
        elif node_type == 'end':
            print(f"\n{text}\n")
        
        elif node_type == 'decision':
            # Shouldn't be called directly
            pass
        
        return choice_index
    
    def display_final_state(self):
        """Show accumulated state"""
        print("\n" + "="*70)
        print("SESSION STATISTICS")
        print("="*70)
        print(f"Axis 1 (Locus of Control):")
        print(f"  Internal (you control): {self.state['axis1']['internal']}")
        print(f"  External (circumstances): {self.state['axis1']['external']}")
        print(f"\nAxis 2 (Contribution):")
        print(f"  Contribution (giving): {self.state['axis2']['contribution']}")
        print(f"  Entitlement (expecting): {self.state['axis2']['entitlement']}")
        print(f"\nAxis 3 (Radius of Concern):")
        print(f"  Self-centric: {self.state['axis3']['self']}")
        print(f"  Other-centric: {self.state['axis3']['other']}")
        print("="*70 + "\n")

def main():
    tree_file = 'refelction-tree.json'
    
    if not os.path.exists(tree_file):
        print(f"Error: {tree_file} not found.")
        return
    
    print("\n" + "="*70)
    print("THE DAILY REFLECTION TREE - TEST RUN")
    print("="*70)
    print("\n--- PERSONA 1: Victim/Self-Centric Path ---\n")
    
    # Persona 1: External locus, entitlement, self-centric
    # Choices: C(someday), B(blame others), A(alone), A(defensive), B(discouraged), A(help friend)
    persona1_choices = [2, 1, 0, 0, 1, 0]  # 0-indexed
    
    agent1 = ReflectionAgentTest(tree_file)
    agent1.walk_tree(auto_choices=persona1_choices)
    agent1.display_final_state()
    
    print("\n" + "="*70)
    print("\n--- PERSONA 2: Victor/Other-Centric Path ---\n")
    
    # Persona 2: Internal locus, contribution, other-centric
    # Choices: B(start now), A(freeing), A(guilt/owned), A(connected/friend), B(independent), A(inspired/action), B(fairness)
    persona2_choices = [1, 0, 0, 0, 0, 0, 1]  # 0-indexed
    
    agent2 = ReflectionAgentTest(tree_file)
    agent2.walk_tree(auto_choices=persona2_choices)
    agent2.display_final_state()

if __name__ == '__main__':
    main()