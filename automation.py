import re
import os
from collections import defaultdict

def read_file(filename):
    """Read content from file safely"""
    if not os.path.exists(filename):
        print("❌ Error: File does not exist.")
        return None
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print("❌ Error reading file:", e)
        return None


def extract_emails(text):
    """Extract emails using regex"""
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    emails = re.findall(email_pattern, text)
    return emails


def analyze_domains(emails):
    """Count emails by domain"""
    domain_count = defaultdict(int)
    
    for email in emails:
        domain = email.split("@")[1]
        domain_count[domain] += 1
    
    return domain_count


def save_results(unique_emails, domain_stats, output_file):
    """Save extracted emails and summary"""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("📧 Extracted Email Addresses\n")
        file.write("=" * 40 + "\n")
        
        for email in unique_emails:
            file.write(email + "\n")
        
        file.write("\n📊 Domain Summary\n")
        file.write("=" * 40 + "\n")
        
        for domain, count in domain_stats.items():
            file.write(f"{domain} : {count}\n")
        
        file.write("\nTotal Unique Emails: " + str(len(unique_emails)))


def main():
    input_file = "input.txt"
    output_file = "email_report.txt"

    print("🔍 Email Extraction Automation Script")
    print("-" * 40)

    content = read_file(input_file)

    if content is None:
        return

    emails = extract_emails(content)

    if not emails:
        print("⚠ No email addresses found.")
        return

    unique_emails = list(set(emails))
    domain_stats = analyze_domains(unique_emails)

    save_results(unique_emails, domain_stats, output_file)

    print(f"✅ {len(unique_emails)} unique emails extracted.")
    print("📁 Results saved to email_report.txt")


if __name__ == "__main__":
    main()
