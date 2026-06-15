# Cryptography — RAM Key Extraction & DES Encryption

## Executive Summary

This project demonstrates applied knowledge of cryptographic principles, memory forensics, and secure coding practices in C#. The work investigates the full lifecycle of DES encryption keys — from generation and pinning in memory, through active use, to attempted secure erasure — and critically examines where managed-language environments fall short of true key hygiene.

Using FTK Imager and HxD, the project performs live RAM dump analysis to locate and verify DES key material in memory at the byte level. The investigation surfaces a significant limitation of the .NET CLR: even after explicit key-wiping logic (`GCHandle`, `Array.Clear`), the Windows Cryptographic Service Provider layer retains internal managed buffers that are outside developer control, leaving residual key material in memory.

The deliverables include a slide deck presenting the technical findings and a recorded walkthrough demonstrating the methodology end to end.

**Key skills demonstrated:** cryptographic key management, memory forensics, secure coding in C#, debugging with breakpoints, RAM dump analysis, and clear communication of nuanced technical limitations to a non-specialist audience.
