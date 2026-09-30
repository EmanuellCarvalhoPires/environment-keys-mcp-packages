---
tags:
  - moc
  - mcp
  - api/app/automation
up: "[[MCP Tools]]"
---
# MCP - Automation

- **Tools:** 17 (exposed: 6; the others via `run_vault_tool`)
- **Requests only:** 0
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/automation/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Manual rules

- [[automation_search_for_manual_rules]] — `GET /rest/v1/rule/manual/search` — Search for manual rules
- [[automation_search_for_manual_rules_post]] — `POST /rest/v1/rule/manual/search` — Search for manual rules ⭐
- [[automation_invoke_a_manual_rule]] — `POST /rest/v1/rule/manual/{ruleId}/invocation` — Invoke a manual rule ✏️⭐

## Rule management

- [[automation_find_rules]] — script over `GET /rest/v1/rule/summary` — Find rules by project, global or project-type scope, state, name and label (compact result, internal pagination) ⭐
- [[automation_search_rule_config]] — script over `GET /rest/v1/rule/{ruleUuid}` — Find rules whose configuration contains a text (field, smart value, action) ⭐
- [[automation_list_rule_summaries]] — `GET /rest/v1/rule/summary` — List rule summaries ⭐
- [[automation_search_for_rule_summaries]] — `POST /rest/v1/rule/summary` — Search for rule summaries
- [[automation_create_a_new_rule]] — `POST /rest/v1/rule` — Create a new rule ✏️
- [[automation_get_a_rule_by_uuid]] — `GET /rest/v1/rule/{ruleUuid}` — Get a rule by UUID ⭐
- [[automation_update_an_existing_rule]] — `PUT /rest/v1/rule/{ruleUuid}` — Update an existing rule ✏️
- [[automation_delete_disabled_rule]] — `DELETE /rest/v1/rule/{ruleUuid}` — Delete disabled rule ✏️
- [[automation_enable_or_disable_a_rule]] — `PUT /rest/v1/rule/{ruleUuid}/state` — Enable or disable a rule ✏️
- [[automation_update_rule_scope]] — `PUT /rest/v1/rule/{ruleUuid}/rule-scope` — Update rule scope ✏️

## Templates

- [[automation_get_template_by_template_id]] — `GET /rest/v1/template/{templateId}` — Get template by template ID
- [[automation_search_for_templates]] — `GET /rest/v1/template/search` — Search for templates
- [[automation_search_for_templates_post]] — `POST /rest/v1/template/search` — Search for templates
- [[automation_create_a_rule_from_a_template]] — `POST /rest/v1/template/create` — Create a rule from a template ✏️
