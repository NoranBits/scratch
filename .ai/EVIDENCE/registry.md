# EVIDENCE_REGISTRY (L3)
| EVID_ID | TYPE | SOURCE | TRUST_LEVEL | STATUS | SUMMARY | VALIDATION_METHOD | VALIDATED_BY |
|---|---|---|---|---|---|---|---|
| EVID:USER:0001 | NOTE | User Approval | FACT | ACTIVE | APPROVE command issued by user. | n/a | user |
| EVID:USER:0002 | NOTE | User Direction | FACT | ACTIVE | Policy Update: APPROVE only for high-level decisions. | n/a | user |
| EVID:BOOT:001 | DOC | INDEX.md | FACT | ACTIVE | Bootstrap OK. | sha256=2EF8376713547716576EB33BDFBDAD2302FC96203612B0F7AD94FE20A56E5CF5 | field_agent |
| EVID:BOOT:002 | DOC | STATE/stable_state.md | FACT | ACTIVE | Root anchor. | sha256=A1A63C50BDFF6B795EE690BE9B3AFFCBC2BFF8D5046D8EDDCC4D6EB5C05CE52F | field_agent |
| EVID:BOOT:003 | DOC | TASKS/active_task.md | FACT | ACTIVE | Task definition. | sha256=6615B6E9A5918CDA5987F6019D512FEE78C9224D3650EBEBDB7F868BB9DE1ACA | field_agent |
| EVID:BOOT:004 | DOC | adk_init_report.md | FACT | ACTIVE | ADK code-first pipeline. | sha256=FBF58516F05AAEE30D5B5728E6087332469F6E7567B9F57F113B94D1C687B0CB | field_agent |
| EVID:FED:001 | DOC | FEDERATION/INDEX.md | VERIFY | ACTIVE | Template init. | sha256=09730E845BA115D83D33F0EA17FC0BBA2A0BFC89BF12374724DE182E0C98D611 | field_agent |
| EVID:FED:002 | DOC | FEDERATION/peers.md | VERIFY | ACTIVE | Peers init. | sha256=42F5C4AFBA07D51F9FC10AF60ACB0B31335E0B04242184C21BCFB97A9ABCF34E | field_agent |
| EVID:FED:003 | DOC | FEDERATION/status_export.md | VERIFY | ACTIVE | Status export init. | sha256=1A6518F46990D737E8F82B37DB6DFD109BD98D81C1D95875AB0D9EE1B73F8838 | field_agent |

*Note: Runtime peer links generated during handshake execution (e.g., `EVID:FED:PEER_ALPHA`) are mapped sequentially to the `EVID:FED:001-003+` naming scheme in their respective target local registries for alias consistency.*
