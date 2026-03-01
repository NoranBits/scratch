# CAPABILITY PROMOTION GATE (TEMPLATE)
**Schema**: `07_SCHEMA_CAPABILITY_PROMOTION`
**Purpose**: Standardized structure to promote a Tool / Adapter from `VERIFY` to `FACT` trust level, strictly based on execution evidence.

## Tool Identifier
- **Tool Name / ID**: `<TOOL_NAME_OR_CAP_ID>`
- **Current Status**: `<VERIFY | UNKNOWN>`
- **Target Status**: `FACT`

## Test Execution Evidence (MUST)
*To promote a capability, the Field Agent MUST provide explicit evidence of successful execution in the repository context.*

- **Test Description**: `<What was tested? Example: "Dry run of negative testing against L1 files">`
- **Execution Log / Payload**: 
  - `<Link to RETURN_PACKET or executed command string>`
- **EVID_ID Reference**: `<EVID:TEST:YYYYMMDD:NNNN>`

## Rollback & Risk Assessment
- **Failure Mode**: `<What happens if this tool hallucinates or fails?>`
- **Rollback Strategy**: `<How do we revert changes made by this tool? Example: "Git checkout / Restore from STREAMS archive">`

## Governance Approval
- **Validation Method**: `<test | diff | log_analysis>`
- **Promoted By**: `<Field Agent ID / User>`
- **Date Promoted**: `<YYYY-MM-DDTHH:MM:SSZ>`
