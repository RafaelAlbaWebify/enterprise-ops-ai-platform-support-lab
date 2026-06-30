# Initial VirtualBox Scenarios

These scenarios are intentionally practical and support-oriented. Each one should produce evidence, a ticket note and a short documentation improvement.

## Scenario 1 - DNS Record Mismatch

### Situation

A user reports that an internal application opens from one machine but not from another.

### Practice Goal

Validate name resolution, compare expected and actual DNS results, and document the finding without jumping to conclusions.

### Evidence To Capture

- affected hostname or application alias
- client IP configuration
- DNS server in use
- forward lookup result
- reverse lookup result, if applicable
- ping or connectivity result, if relevant
- final ticket note

### Support Skills Demonstrated

- DNS troubleshooting
- symptom scoping
- evidence collection
- escalation-ready notes

## Scenario 2 - Group Membership Access Issue

### Situation

A user can log in but cannot access a shared folder or internal resource.

### Practice Goal

Check user identity, group membership, permissions and access path before changing anything.

### Evidence To Capture

- user account checked
- expected access group
- current group membership
- resource path
- permission finding
- action taken or escalation recommendation

### Support Skills Demonstrated

- identity and access troubleshooting
- permissions reasoning
- safe validation before escalation

## Scenario 3 - Windows Client Baseline Drift

### Situation

A Windows client behaves differently from the expected baseline after configuration changes or updates.

### Practice Goal

Collect system evidence and compare it against expected support baseline.

### Evidence To Capture

- OS version
- hostname
- IP configuration
- disk space
- relevant services
- recent system errors
- remediation or next step

### Support Skills Demonstrated

- endpoint support
- PowerShell evidence collection
- baseline comparison

## Scenario 4 - Service Unavailable

### Situation

A simple internal service is unavailable from the client machine.

### Practice Goal

Separate service state, host connectivity, name resolution and firewall assumptions.

### Evidence To Capture

- service status
- server reachability
- port or application check
- DNS result
- event or log entry
- final support summary

### Support Skills Demonstrated

- structured troubleshooting
- dependency isolation
- escalation clarity

## Scenario 5 - Ticket To KB Workflow

### Situation

A repeated support issue has been solved more than once but is still not documented clearly.

### Practice Goal

Turn a ticket resolution into a short knowledge base article or runbook.

### Evidence To Capture

- original ticket symptom
- checks performed
- final fix or workaround
- validation step
- KB article draft
- runbook improvement note

### Support Skills Demonstrated

- documentation discipline
- service improvement
- repeatable support process