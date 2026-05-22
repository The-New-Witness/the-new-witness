# Security Policy — The New Witness

## System Classification

The New Witness is a **sovereign data archival system** operating under the governance protocols defined in `.codexrules.md`. This system handles sensitive resistance tracking data, emotional memory records, and immutable truth archives. Security of this system is paramount to the integrity of its archival mission.

All usage permissions and IP governance are defined in `.codexrules.md` and the repository LICENSE. This security policy operates in conjunction with those documents.

## Reporting a Vulnerability

**DO NOT** open a public GitHub issue for security vulnerabilities.

If you discover a security vulnerability in The New Witness system, report it exclusively through:

1. **Email:** Send details to **heyhaleybird@gmail.com** with the subject line: `[SECURITY] The New Witness — Vulnerability Report`
2. **GitHub Private Vulnerability Reporting:** Use the "Report a vulnerability" button under the Security tab (if enabled).

### What to Include

- A clear description of the vulnerability and which system component is affected (Truth Archive, Emotional Memory Engine, Resistance Tracker, Notion Vault, Deprogrammer)
- Steps to reproduce the issue
- Affected branches or deployment environments
- Potential impact on data integrity, archival immutability, or emotional memory records
- Any suggested remediation (optional but appreciated)

## Response Timeline

| Action | Timeframe |
|--------|-----------|
| Acknowledgment of report | Within 48 hours |
| Initial assessment and triage | Within 5 business days |
| Patch for critical/data-integrity issues | Within 30 days |
| Patch for non-critical issues | Within 90 days |
| Public disclosure | After patch + minimum 30 days post-deployment |

## Disclosure Policy

- **Strict coordinated disclosure**: Do NOT publicly disclose any vulnerability until an official patch has been released and a minimum of 30 days has passed since the fix was deployed.
- The New Witness handles sensitive archival data. Premature disclosure that could compromise data integrity, resistance tracking records, or emotional memory archives will be treated as a hostile act and may result in legal action under applicable IP and data protection laws.
- Credit will be given to reporters (unless anonymity is requested) once the fix is public.

## Scope — Protected Components

This security policy applies to all components of The New Witness system:

| Component | Description | Security Priority |
|-----------|-------------|-------------------|
| **Truth Archive** | Immutable data persistence layer for verified records | CRITICAL |
| **Emotional Memory Engine** | Processing and storage of qualitative emotional data | CRITICAL |
| **Resistance Tracker** | Monitoring and event tracking subsystem | HIGH |
| **Notion Vault** | Structured database schema and embed cards | HIGH |
| **Deprogrammer** | Media/cognitive distortion analysis module | MEDIUM |
| **Deploy Pipeline** | Replit deployment and infrastructure scripts | MEDIUM |
| **Frontend Modules** | Tracker UI, Emotional Visualizer, Shared Styles | MEDIUM |

### Critical Data Assets

The following data categories require the highest security protections:

- Archival records within the Truth Archive (immutability violations are CRITICAL severity)
- Emotional memory data and associated processing logic
- Resistance event logs and tracking metadata
- Notion API integration tokens and vault access credentials
- Any data that could identify subjects of resistance tracking

### Out of Scope

- Vulnerabilities in the Notion platform itself (report to Notion)
- Vulnerabilities in Replit infrastructure (report to Replit)
- Social engineering attacks against the maintainer
- General denial of service against hosted infrastructure

## Supported Versions

Only the `main` branch and actively deployed instances receive security updates.

## Security Standards

The New Witness enforces the following security practices in alignment with its sovereign IP governance:

1. **Archive Immutability**: Once committed to the Truth Archive, records must not be modifiable or deletable. Any mechanism that could bypass immutability is a critical vulnerability.
2. **No secrets in code**: API keys (especially Notion integration tokens), passwords, and credentials must NEVER be committed to the repository.
3. **Data classification**: All data handled by the system is classified and treated according to its sensitivity level as defined above.
4. **Least privilege**: All integrations (Notion API, deployment scripts) operate with minimum required permissions.
5. **Integrity verification**: Archival records should be verifiable against tampering.
6. **No unauthorized data collection**: This system does not collect or transmit data beyond its defined archival scope.
7. **Emotional data protection**: Emotional memory records are treated as sensitive personal data regardless of jurisdiction.

## Prohibited Actions

The following actions are strictly prohibited and will result in legal action under the full extent of applicable law, including but not limited to IP theft, unauthorized access, and data protection violations:

- Unauthorized access to the Truth Archive, Emotional Memory Engine, or any system component
- Any attempt to modify, corrupt, or destroy immutable archival records
- Exfiltration of emotional memory data, resistance tracking records, or vault contents
- Exploitation of vulnerabilities beyond minimal proof-of-concept demonstration
- Reverse engineering of proprietary algorithms (cognitive distortion analysis, emotional processing)
- Automated vulnerability scanning without prior written consent
- Any action that compromises the anonymity or safety of subjects in resistance tracking data
- Social engineering or phishing attacks against the maintainer or system operators
- Unauthorized reproduction or distribution of system architecture, algorithms, or data schemas

## Safe Harbor

Responsible security research is supported under the following conditions:

- We will not pursue legal action against researchers who comply with this policy
- We will work collaboratively to understand and resolve reported issues
- We will publicly acknowledge contributions (if desired) once fixes are deployed

**Safe harbor applies ONLY if:**
- You report exclusively through the channels listed above
- You do not access, modify, or exfiltrate any actual archival data, emotional memory records, or resistance tracking information
- You do not exploit any vulnerability beyond minimal proof-of-concept
- You do not violate any laws in the process
- You allow reasonable time for resolution before any disclosure
- You comply with the governance protocols in `.codexrules.md`

## Intellectual Property & Legal Notice

All code, architecture, algorithms, data schemas, and intellectual property within The New Witness repository is the exclusive property of **Haley Ann Bird**, governed under the sovereign IP framework defined in `.codexrules.md` and the repository LICENSE ("All rights reserved").

The following are expressly protected:
- The Truth Archive architecture and immutability mechanisms
- The Emotional Memory Engine and its processing logic
- The Resistance Tracker event monitoring system
- The Deprogrammer cognitive distortion analysis methodology
- All Notion Vault schemas, templates, and integration logic
- The "New Witness" name, concept, and system design

Unauthorized reproduction, distribution, reverse engineering, or commercial use of any proprietary component discovered during security research is strictly prohibited and will be prosecuted to the fullest extent of applicable law.

This security policy operates under and is subordinate to the governance framework established in `.codexrules.md`.

---

**Last updated:** 2026-05-18
**Policy version:** 1.0
**System:** The New Witness — Truth Archive & Emotional Memory Engine
**Maintainer:** Haley Ann Bird (heyhaleybird@gmail.com)
**Governance:** `.codexrules.md` | LICENSE (All Rights Reserved)
# Security Policy

## Overview

The security of this project and its users is a top priority. This document outlines our security policy, vulnerability reporting process, and security best practices.
This repository is owned and maintained by Haley Ann Bird. The security of this project and its users is taken seriously. This document outlines the security policy, vulnerability reporting process, and best practices for this project.

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

**Do not** open a public GitHub issue for security vulnerabilities.

**Contact:** heyhaleybird@gmail.com
**Subject line:** `[SECURITY] the-new-witness vulnerability report`

Please include the following in your report:
- Description of the vulnerability
- Steps to reproduce the issue
- Potential impact assessment
- Any suggested remediation
- Your contact information for follow-up

## Response Timeline

- **Acknowledgment:** Within 72 hours of receiving your report
- **Initial assessment:** Within 7 days
- **Resolution timeline:** Provided after initial assessment
- **Credit:** Responsible disclosures will be credited (with your permission)
### How to Report

1. **Email**: Send a detailed report to security@haleybirddesign.com
2. **Subject Line**: `[SECURITY] the-new-witness vulnerability report`
3. **Include**:
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact assessment
   - Any suggested remediation
   - Your contact information for follow-up

### Response Timeline

- **Acknowledgment**: Within 72 hours of receipt
- **Initial Assessment**: Within 7 business days
- **Resolution Timeline**: Provided after initial assessment
- **Status Updates**: At least every 14 days until resolved

## Supported Versions

| Version | Supported |
| ------- | --------- |
| Latest  | Yes       |

## Security Best Practices

This project follows these security principles:
- No API keys, tokens, or credentials are stored in the repository
- Dependencies are regularly reviewed and updated
- Code changes are reviewed before merging
- Sensitive data is never committed to version control

## Intellectual Property Protection

This project contains proprietary intellectual property owned by Haley Ann Bird. All code, algorithms, architectures, and documentation are protected under applicable intellectual property laws. Unauthorized access, reproduction, or distribution may result in legal action.
|---------|-----------|
| Latest  | Yes       |
| Older   | Case-by-case |

## Security Best Practices

### For Contributors

- Never commit sensitive data (API keys, passwords, tokens, credentials)
- Use environment variables for all sensitive configuration
- Follow the principle of least privilege in all code
- Keep dependencies up to date and review security advisories
- Use signed commits when possible

### For Users

- Keep your local copy up to date with the latest releases
- Report any suspicious behavior or potential vulnerabilities
- Do not attempt to exploit vulnerabilities for malicious purposes
- Follow responsible disclosure practices

## What Is NOT in This Repository

For security reasons, the following are intentionally absent from this repository:

- API keys, tokens, or credentials of any kind
- Proprietary training data or model weights
- Full patent claim language (pending filings)
- Commercial contract details or investor materials
- Personal user data of any kind

## Intellectual Property Protection

This project contains proprietary intellectual property owned by Haley Ann Bird. All code, designs, algorithms, and documentation are protected under applicable intellectual property laws. Unauthorized access, reproduction, or distribution may result in legal action.

For details, see:
- [LICENSE](LICENSE)
- [COPYRIGHT_AND_ATTRIBUTIONS.md](COPYRIGHT_AND_ATTRIBUTIONS.md)
- [TRADEMARK.md](TRADEMARK.md)
- [PATENT.md](PATENT.md)

## Responsible Disclosure

We commit to:
- Acknowledging reports within 72 hours
- Providing a resolution timeline within 7 days
- Crediting responsible disclosures (with permission)
- Never pursuing legal action against good-faith security researchers

## Contact

For all security-related inquiries:
- **Email:** heyhaleybird@gmail.com

---

*Last updated: May 2026*
- Providing a resolution timeline within 7 business days
- Crediting responsible disclosures (with permission)
- Never pursuing legal action against good-faith security researchers

## Contact Information

- **Security**: heyhaleybird@gmail.com
- **Legal**: heyhaleybird@gmail.com
- **General**: heyhaleybird@gmail.com

---

*Last Updated: May 2026*
