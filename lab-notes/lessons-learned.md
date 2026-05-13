# Lessons Learned

## Purpose

Capture practical lessons from the lab and convert them into better support documentation.

### Lesson 001

Date: 2026-05-13

Scenario: Initial validation of support scripts.

What happened: I tested the basic PowerShell and Python support scripts locally.

What I checked:

- Windows service status for Spooler and WinRM.
- Windows support snapshot including OS version, uptime, disk space, network adapters, stopped automatic services and recent system errors.
- Simulated AI Platform API error explanations for HTTP 200, 400, 401, 403, 429 and 500.
- Basic external endpoint health check against https://www.microsoft.com.

Results:

- Spooler was running and set to Automatic.
- WinRM was stopped and set to Manual. This is not automatically an incident unless remote management is expected.
- The workstation had healthy free disk space.
- The active Wi-Fi adapter had a valid LAN IP address.
- Some inactive adapters showed 169.254.x.x link-local addresses, which is expected if they are not connected.
- No recent system errors were returned by the script.
- The simulated AI API error script worked as expected.
- The Microsoft endpoint returned HTTP 200 with approximately 283 ms latency.

What I learned:

Small support scripts can make triage more consistent by collecting repeatable evidence before escalation. However, script output must be interpreted carefully. A stopped service, an automatic service not currently running, or a link-local IP address is not automatically an incident without business impact or expected service behaviour.

What documentation should be improved:

- Add example outputs to the script documentation.
- Improve network output formatting in the Windows support snapshot script.
- Add a note explaining that some stopped automatic Windows services may be normal.
- Add a support interpretation section for WinRM being stopped when startup type is Manual.
