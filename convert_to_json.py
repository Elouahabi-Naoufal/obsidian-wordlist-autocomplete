#!/usr/bin/env python3

import os
import json
import re
from pathlib import Path

def parse_txt_file(file_path, domain_name):
    """Parse a txt file and extract words with their categories"""
    words_data = {}
    current_category = None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Check if line is a category header (starts with #)
            if line.startswith('#'):
                current_category = line[1:].strip()
                continue
            
            # Add word with domain and category info
            if current_category and line:
                words_data[line] = {
                    "domain": domain_name,
                    "category": current_category
                }
    
    return words_data

def get_domain_name(filename):
    """Convert filename to readable domain name"""
    domain_mapping = {
        'cloud_computing.txt': 'Cloud Computing',
        'cybersecurity.txt': 'Cybersecurity',
        'database_management.txt': 'Database Management',
        'data_science_analytics.txt': 'Data Science/Analytics',
        'devops.txt': 'DevOps',
        'it_support_helpdesk.txt': 'IT Support/Help Desk',
        'mobile_development.txt': 'Mobile Development',
        'network_administration.txt': 'Network Administration',
        'quality_assurance.txt': 'Quality Assurance',
        'software_development.txt': 'Software Development',
        'system_administration.txt': 'System Administration',
        'web_development.txt': 'Web Development'
    }
    return domain_mapping.get(filename, filename.replace('.txt', '').replace('_', ' ').title())

def main():
    # Input and output directories
    input_dir = Path('IT')
    output_dir = Path('IT_to_json')
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Combined dictionary for all domains
    all_words = {}
    
    # Process each txt file in IT directory
    for txt_file in input_dir.glob('*.txt'):
        print(f"Processing {txt_file.name}...")
        
        domain_name = get_domain_name(txt_file.name)
        words_data = parse_txt_file(txt_file, domain_name)
        
        # Save individual domain JSON
        domain_json_file = output_dir / f"{txt_file.stem}.json"
        with open(domain_json_file, 'w', encoding='utf-8') as f:
            json.dump(words_data, f, indent=2, ensure_ascii=False)
        
        print(f"  - Created {domain_json_file}")
        print(f"  - Words: {len(words_data)}")
        
        # Add to combined dictionary
        all_words.update(words_data)
    
    # Save combined JSON file
    combined_json_file = output_dir / 'all_it_domains.json'
    with open(combined_json_file, 'w', encoding='utf-8') as f:
        json.dump(all_words, f, indent=2, ensure_ascii=False)
    
    print(f"\nCreated combined file: {combined_json_file}")
    print(f"Total unique words: {len(all_words)}")
    
    # Create summary statistics
    domain_stats = {}
    category_stats = {}
    
    for word, info in all_words.items():
        domain = info['domain']
        category = info['category']
        
        # Count by domain
        if domain not in domain_stats:
            domain_stats[domain] = 0
        domain_stats[domain] += 1
        
        # Count by category
        category_key = f"{domain} - {category}"
        if category_key not in category_stats:
            category_stats[category_key] = 0
        category_stats[category_key] += 1
    
    # Save statistics
    stats = {
        'total_words': len(all_words),
        'domains': domain_stats,
        'categories': category_stats
    }
    
    stats_file = output_dir / 'statistics.json'
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print(f"Created statistics file: {stats_file}")
    
    # Print summary
    print(f"\n=== SUMMARY ===")
    print(f"Total words processed: {len(all_words)}")
    print(f"Domains: {len(domain_stats)}")
    print(f"Categories: {len(category_stats)}")
    print(f"\nWords per domain:")
    for domain, count in sorted(domain_stats.items(), key=lambda x: x[1], reverse=True):
        print(f"  {domain}: {count}")

if __name__ == "__main__":
    main()