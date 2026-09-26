---
tags:
  - moc
  - mcp
  - api/app/jsm-ops
up: "[[MCP Tools]]"
---
# MCP - JSM Ops

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 240
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/jira/service-desk-ops/rest/v2/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Alerts

- [[JSM Ops - Get request status]] — `GET /api/{cloudId}/v1/alerts/requests/{id}` — Get request status
- [[JSM Ops - List alerts]] — `GET /api/{cloudId}/v1/alerts` — List alerts
- [[JSM Ops - Create alert]] — `POST /api/{cloudId}/v1/alerts` — Create alert ✏️
- [[JSM Ops - Get alert]] — `GET /api/{cloudId}/v1/alerts/{id}` — Get alert
- [[JSM Ops - Delete alert]] — `DELETE /api/{cloudId}/v1/alerts/{id}` — Delete alert ✏️
- [[JSM Ops - Get alert by alias]] — `GET /api/{cloudId}/v1/alerts/alias` — Get alert by alias
- [[JSM Ops - Acknowledge alert]] — `POST /api/{cloudId}/v1/alerts/{id}/acknowledge` — Acknowledge alert ✏️
- [[JSM Ops - Assign alert]] — `POST /api/{cloudId}/v1/alerts/{id}/assign` — Assign alert ✏️
- [[JSM Ops - Add responder to alert]] — `POST /api/{cloudId}/v1/alerts/{id}/responders` — Add responder to alert ✏️
- [[JSM Ops - Add extra properties to alert]] — `POST /api/{cloudId}/v1/alerts/{id}/extra-properties` — Add extra properties to alert ✏️
- [[JSM Ops - Delete extra properties from alert]] — `DELETE /api/{cloudId}/v1/alerts/{id}/extra-properties` — Delete extra properties from alert ✏️
- [[JSM Ops - Add tags to alert]] — `POST /api/{cloudId}/v1/alerts/{id}/tags` — Add tags to alert ✏️
- [[JSM Ops - Delete tags from alert]] — `DELETE /api/{cloudId}/v1/alerts/{id}/tags` — Delete tags from alert ✏️
- [[JSM Ops - Close alert]] — `POST /api/{cloudId}/v1/alerts/{id}/close` — Close alert ✏️
- [[JSM Ops - Escalate alert to next]] — `POST /api/{cloudId}/v1/alerts/{id}/escalate` — Escalate alert to next ✏️
- [[JSM Ops - Execute custom action]] — `POST /api/{cloudId}/v1/alerts/{id}/action` — Execute custom action ✏️
- [[JSM Ops - Snooze alert]] — `POST /api/{cloudId}/v1/alerts/{id}/snooze` — Snooze alert ✏️
- [[JSM Ops - Unacknowledge alert]] — `POST /api/{cloudId}/v1/alerts/{id}/unacknowledge` — Unacknowledge alert ✏️
- [[JSM Ops - List alert notes]] — `GET /api/{cloudId}/v1/alerts/{id}/notes` — List alert notes
- [[JSM Ops - Add alert note]] — `POST /api/{cloudId}/v1/alerts/{id}/notes` — Add alert note ✏️
- [[JSM Ops - Delete alert note]] — `DELETE /api/{cloudId}/v1/alerts/{alertId}/notes/{id}` — Delete alert note ✏️
- [[JSM Ops - Update alert note]] — `PATCH /api/{cloudId}/v1/alerts/{alertId}/notes/{id}` — Update alert note ✏️
- [[JSM Ops - Update alert priority]] — `PATCH /api/{cloudId}/v1/alerts/{id}/priority` — Update alert priority ✏️
- [[JSM Ops - Update alert message]] — `PATCH /api/{cloudId}/v1/alerts/{id}/message` — Update alert message ✏️
- [[JSM Ops - Update alert description]] — `PATCH /api/{cloudId}/v1/alerts/{id}/description` — Update alert description ✏️
- [[JSM Ops - List alert logs]] — `GET /api/{cloudId}/v1/alerts/{id}/logs` — List alert logs
- [[JSM Ops - List attachments for alert]] — `GET /api/{cloudId}/v1/alerts/{alertId}/attachments` — List attachments for alert
- [[JSM Ops - Add attachment to alert]] — `POST /api/{cloudId}/v1/alerts/{alertId}/attachments` — Add attachment to alert ✏️📎
- [[JSM Ops - Get attachment download URL]] — `GET /api/{cloudId}/v1/alerts/{alertId}/attachments/{id}` — Get attachment download URL
- [[JSM Ops - Delete attachment]] — `DELETE /api/{cloudId}/v1/alerts/{alertId}/attachments/{id}` — Delete attachment ✏️

## Audit Logs

- [[JSM Ops - Get audit Logs]] — `GET /api/{cloudId}/v1/logs` — Get audit Logs

## Contacts

- [[JSM Ops - List contacts]] — `GET /api/{cloudId}/v1/users/contacts` — List contacts
- [[JSM Ops - Create contact]] — `POST /api/{cloudId}/v1/users/contacts` — Create contact ✏️
- [[JSM Ops - Activate contact]] — `PATCH /api/{cloudId}/v1/users/contacts/{id}/activate` — Activate contact ✏️
- [[JSM Ops - Deactivate contact]] — `PATCH /api/{cloudId}/v1/users/contacts/{id}/deactivate` — Deactivate contact ✏️
- [[JSM Ops - Get contact]] — `GET /api/{cloudId}/v1/users/contacts/{id}` — Get contact
- [[JSM Ops - Delete contact]] — `DELETE /api/{cloudId}/v1/users/contacts/{id}` — Delete contact ✏️
- [[JSM Ops - Update contact]] — `PATCH /api/{cloudId}/v1/users/contacts/{id}` — Update contact ✏️

## Custom user roles

- [[JSM Ops - Get custom user role]] — `GET /api/{cloudId}/v1/roles/{identifier}` — Get custom user role
- [[JSM Ops - Update custom user role]] — `PUT /api/{cloudId}/v1/roles/{identifier}` — Update custom user role ✏️
- [[JSM Ops - Delete custom user role]] — `DELETE /api/{cloudId}/v1/roles/{identifier}` — Delete custom user role. ✏️
- [[JSM Ops - Assign custom user role]] — `POST /api/{cloudId}/v1/roles/assign` — Assign custom user role ✏️
- [[JSM Ops - List custom user roles]] — `GET /api/{cloudId}/v1/roles` — List custom user roles
- [[JSM Ops - Create custom user role]] — `POST /api/{cloudId}/v1/roles` — Create custom user role ✏️

## Escalations

- [[JSM Ops - List escalations]] — `GET /api/{cloudId}/v1/teams/{teamId}/escalations` — List escalations
- [[JSM Ops - Create escalation]] — `POST /api/{cloudId}/v1/teams/{teamId}/escalations` — Create escalation ✏️
- [[JSM Ops - Get escalation]] — `GET /api/{cloudId}/v1/teams/{teamId}/escalations/{id}` — Get escalation
- [[JSM Ops - Delete escalation]] — `DELETE /api/{cloudId}/v1/teams/{teamId}/escalations/{id}` — Delete escalation ✏️
- [[JSM Ops - Update escalation]] — `PATCH /api/{cloudId}/v1/teams/{teamId}/escalations/{id}` — Update escalation ✏️

## Forwarding rules

- [[JSM Ops - List forwarding rules]] — `GET /api/{cloudId}/v1/forwarding-rules` — List forwarding rules
- [[JSM Ops - Create forwarding rule]] — `POST /api/{cloudId}/v1/forwarding-rules` — Create forwarding rule ✏️
- [[JSM Ops - Get forwarding rule]] — `GET /api/{cloudId}/v1/forwarding-rules/{id}` — Get forwarding rule
- [[JSM Ops - Update forwarding rule]] — `PUT /api/{cloudId}/v1/forwarding-rules/{id}` — Update forwarding rule ✏️
- [[JSM Ops - Delete forwarding rule]] — `DELETE /api/{cloudId}/v1/forwarding-rules/{id}` — Delete forwarding rule ✏️

## Heartbeats

- [[JSM Ops - List heartbeats]] — `GET /api/{cloudId}/v1/teams/{teamId}/heartbeats` — List heartbeats
- [[JSM Ops - Create heartbeat]] — `POST /api/{cloudId}/v1/teams/{teamId}/heartbeats` — Create heartbeat ✏️
- [[JSM Ops - Delete heartbeat]] — `DELETE /api/{cloudId}/v1/teams/{teamId}/heartbeats` — Delete heartbeat ✏️
- [[JSM Ops - Update heartbeat]] — `PATCH /api/{cloudId}/v1/teams/{teamId}/heartbeats` — Update heartbeat ✏️
- [[JSM Ops - Ping Heartbeat]] — `GET /api/{cloudId}/v1/teams/{teamId}/heartbeats/ping` — Ping Heartbeat

## Integrations

- [[JSM Ops - List integrations]] — `GET /api/{cloudId}/v1/integrations` — List integrations
- [[JSM Ops - Create integration]] — `POST /api/{cloudId}/v1/integrations` — Create integration ✏️
- [[JSM Ops - Get integration]] — `GET /api/{cloudId}/v1/integrations/{id}` — Get integration
- [[JSM Ops - Delete integration]] — `DELETE /api/{cloudId}/v1/integrations/{id}` — Delete integration ✏️
- [[JSM Ops - Update integration]] — `PATCH /api/{cloudId}/v1/integrations/{id}` — Update integration ✏️

## Integration actions

- [[JSM Ops - List integration actions]] — `GET /api/{cloudId}/v1/integrations/{integrationId}/actions` — List integration actions
- [[JSM Ops - Create integration action]] — `POST /api/{cloudId}/v1/integrations/{integrationId}/actions` — Create integration action ✏️
- [[JSM Ops - Get integration action]] — `GET /api/{cloudId}/v1/integrations/{integrationId}/actions/{id}` — Get integration action
- [[JSM Ops - Delete integration action]] — `DELETE /api/{cloudId}/v1/integrations/{integrationId}/actions/{id}` — Delete integration action ✏️
- [[JSM Ops - Update integration action]] — `PATCH /api/{cloudId}/v1/integrations/{integrationId}/actions/{id}` — Update integration action ✏️
- [[JSM Ops - Reorder integration action]] — `PATCH /api/{cloudId}/v1/integrations/{integrationId}/actions/{id}/order` — Reorder integration action ✏️

## Integration outgoing filters

- [[JSM Ops - Get integration alert filter]] — `GET /api/{cloudId}/v1/integrations/{integrationId}/outgoing/alert-filter/main` — Get integration alert filter
- [[JSM Ops - Update integration alert filter]] — `PATCH /api/{cloudId}/v1/integrations/{integrationId}/outgoing/alert-filter/main` — Update integration alert filter ✏️

## Maintenances

- [[JSM Ops - List global maintenances]] — `GET /api/{cloudId}/v1/maintenances` — List global maintenances
- [[JSM Ops - Create global maintenance]] — `POST /api/{cloudId}/v1/maintenances` — Create global maintenance ✏️
- [[JSM Ops - Get global maintenance]] — `GET /api/{cloudId}/v1/maintenances/{id}` — Get global maintenance
- [[JSM Ops - Deletes global maintenance]] — `DELETE /api/{cloudId}/v1/maintenances/{id}` — Deletes global maintenance ✏️
- [[JSM Ops - Update global maintenance]] — `PATCH /api/{cloudId}/v1/maintenances/{id}` — Update global maintenance ✏️
- [[JSM Ops - Cancel global maintenance]] — `POST /api/{cloudId}/v1/maintenances/{id}/cancel` — Cancel global maintenance ✏️
- [[JSM Ops - List team maintenances]] — `GET /api/{cloudId}/v1/teams/{teamId}/maintenances` — List team maintenances
- [[JSM Ops - Create team maintenance]] — `POST /api/{cloudId}/v1/teams/{teamId}/maintenances` — Create team maintenance ✏️
- [[JSM Ops - Get team maintenance]] — `GET /api/{cloudId}/v1/teams/{teamId}/maintenances/{id}` — Get team maintenance
- [[JSM Ops - Delete team maintenance]] — `DELETE /api/{cloudId}/v1/teams/{teamId}/maintenances/{id}` — Delete team maintenance ✏️
- [[JSM Ops - Update team maintenance]] — `PATCH /api/{cloudId}/v1/teams/{teamId}/maintenances/{id}` — Update team maintenance ✏️
- [[JSM Ops - Cancel team maintenance]] — `POST /api/{cloudId}/v1/teams/{teamId}/maintenances/{id}/cancel` — Cancel team maintenance ✏️

## Notification rules

- [[JSM Ops - List notification rules]] — `GET /api/{cloudId}/v1/notification-rules` — List notification rules
- [[JSM Ops - Create notification rule]] — `POST /api/{cloudId}/v1/notification-rules` — Create notification rule ✏️
- [[JSM Ops - Get notification rule]] — `GET /api/{cloudId}/v1/notification-rules/{id}` — Get notification rule
- [[JSM Ops - Delete notification rule]] — `DELETE /api/{cloudId}/v1/notification-rules/{id}` — Delete notification rule ✏️
- [[JSM Ops - Update notification rule]] — `PATCH /api/{cloudId}/v1/notification-rules/{id}` — Update notification rule ✏️

## Notification rule steps

- [[JSM Ops - List notification rule steps]] — `GET /api/{cloudId}/v1/notification-rules/{ruleId}/steps` — List notification rule steps
- [[JSM Ops - Create notification rule step]] — `POST /api/{cloudId}/v1/notification-rules/{ruleId}/steps` — Create notification rule step ✏️
- [[JSM Ops - Get notification rule step]] — `GET /api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}` — Get notification rule step
- [[JSM Ops - Delete notification rule step]] — `DELETE /api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}` — Delete notification rule step ✏️
- [[JSM Ops - Update notification rule step]] — `PATCH /api/{cloudId}/v1/notification-rules/{ruleId}/steps/{id}` — Update notification rule step ✏️

## Policies

- [[JSM Ops - List global alert policies]] — `GET /api/{cloudId}/v1/alerts/policies` — List global alert policies
- [[JSM Ops - Create global alert policy]] — `POST /api/{cloudId}/v1/alerts/policies` — Create global alert policy ✏️
- [[JSM Ops - Get global alert policy]] — `GET /api/{cloudId}/v1/alerts/policies/{policyId}` — Get global alert policy
- [[JSM Ops - Put global alert policy]] — `PUT /api/{cloudId}/v1/alerts/policies/{policyId}` — Put global alert policy ✏️
- [[JSM Ops - Delete global alert policy]] — `DELETE /api/{cloudId}/v1/alerts/policies/{policyId}` — Delete global alert policy ✏️
- [[JSM Ops - Change the order of global alert policy]] — `POST /api/{cloudId}/v1/alerts/policies/{policyId}/change-order` — Change the order of global alert policy ✏️
- [[JSM Ops - Enable the global alert policy]] — `POST /api/{cloudId}/v1/alerts/policies/{policyId}/enable` — Enable the global alert policy ✏️
- [[JSM Ops - Disable the global alert policy]] — `POST /api/{cloudId}/v1/alerts/policies/{policyId}/disable` — Disable the global alert policy ✏️

## Team

- [[JSM Ops - Enable Operations in team]] — `POST /api/{cloudId}/v1/teams/{teamId}/enable-ops` — Enable Operations in team ✏️
- [[JSM Ops - Get status of a team request]] — `GET /api/{cloudId}/v1/teams/{teamId}/requests/{requestId}` — Get status of a team request
- [[JSM Ops - List teams]] — `GET /api/{cloudId}/v1/teams` — List teams

## Team Policies

- [[JSM Ops - List team policies]] — `GET /api/{cloudId}/v1/teams/{teamId}/policies` — List team policies
- [[JSM Ops - Create team policy]] — `POST /api/{cloudId}/v1/teams/{teamId}/policies` — Create team policy ✏️
- [[JSM Ops - Get team policy]] — `GET /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}` — Get team policy
- [[JSM Ops - Put team policy]] — `PUT /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}` — Put team policy ✏️
- [[JSM Ops - Delete global alert policy (DELETE)]] — `DELETE /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}` — Delete global alert policy ✏️
- [[JSM Ops - Change the order of team policy]] — `POST /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}/change-order` — Change the order of team policy ✏️
- [[JSM Ops - Enable the team policy]] — `POST /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}/enable` — Enable the team policy ✏️
- [[JSM Ops - Disable the global alert policy (POST)]] — `POST /api/{cloudId}/v1/teams/{teamId}/policies/{policyId}/disable` — Disable the global alert policy ✏️

## Team roles

- [[JSM Ops - Get Team role]] — `GET /api/{cloudId}/v1/teams/{teamId}/roles/{identifier}` — Get Team role
- [[JSM Ops - Delete a team role]] — `DELETE /api/{cloudId}/v1/teams/{teamId}/roles/{identifier}` — Delete a team role. ✏️
- [[JSM Ops - Update team role]] — `PATCH /api/{cloudId}/v1/teams/{teamId}/roles/{identifier}` — Update team role ✏️
- [[JSM Ops - List Team roles]] — `GET /api/{cloudId}/v1/teams/{teamId}/roles` — List Team roles
- [[JSM Ops - Create team role]] — `POST /api/{cloudId}/v1/teams/{teamId}/roles` — Create team role ✏️

## Routing rules

- [[JSM Ops - List routing rules]] — `GET /api/{cloudId}/v1/teams/{teamId}/routing-rules` — List routing rules
- [[JSM Ops - Create routing rule]] — `POST /api/{cloudId}/v1/teams/{teamId}/routing-rules` — Create routing rule ✏️
- [[JSM Ops - Get routing rule]] — `GET /api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}` — Get routing rule
- [[JSM Ops - Delete routing rule]] — `DELETE /api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}` — Delete routing rule ✏️
- [[JSM Ops - Update routing rule]] — `PATCH /api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}` — Update routing rule ✏️
- [[JSM Ops - Change routing rule order]] — `PATCH /api/{cloudId}/v1/teams/{teamId}/routing-rules/{id}/change-order` — Change routing rule order ✏️

## Schedules

- [[JSM Ops - List schedules]] — `GET /api/{cloudId}/v1/schedules` — List schedules
- [[JSM Ops - Create schedule]] — `POST /api/{cloudId}/v1/schedules` — Create schedule ✏️
- [[JSM Ops - Get schedule]] — `GET /api/{cloudId}/v1/schedules/{id}` — Get schedule
- [[JSM Ops - Delete schedule]] — `DELETE /api/{cloudId}/v1/schedules/{id}` — Delete schedule ✏️
- [[JSM Ops - Update schedule]] — `PATCH /api/{cloudId}/v1/schedules/{id}` — Update schedule ✏️

## Schedule on-calls

- [[JSM Ops - List on-call responders]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}/on-calls` — List on-call responders
- [[JSM Ops - List next on-call responders]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}/next-on-calls` — List next on-call responders
- [[JSM Ops - Export on-call responders]] — `GET /api/{cloudId}/v1/schedules/on-calls/{userIdentifier}.ics` — Export on-call responders 📎

## Schedule overrides

- [[JSM Ops - List overrides]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}/overrides` — List overrides
- [[JSM Ops - Create override]] — `POST /api/{cloudId}/v1/schedules/{scheduleId}/overrides` — Create override ✏️
- [[JSM Ops - Get override]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}` — Get override
- [[JSM Ops - Update override]] — `PUT /api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}` — Update override ✏️
- [[JSM Ops - Delete override]] — `DELETE /api/{cloudId}/v1/schedules/{scheduleId}/overrides/{alias}` — Delete override ✏️

## Schedule rotations

- [[JSM Ops - List rotations]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}/rotations` — List rotations
- [[JSM Ops - Create rotation]] — `POST /api/{cloudId}/v1/schedules/{scheduleId}/rotations` — Create rotation ✏️
- [[JSM Ops - Get rotation]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}/rotations/{id}` — Get rotation
- [[JSM Ops - Delete rotation]] — `DELETE /api/{cloudId}/v1/schedules/{scheduleId}/rotations/{id}` — Delete rotation ✏️
- [[JSM Ops - Update rotation]] — `PATCH /api/{cloudId}/v1/schedules/{scheduleId}/rotations/{id}` — Update rotation ✏️

## Schedule timelines

- [[JSM Ops - Get schedule timeline]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}/timeline` — Get schedule timeline
- [[JSM Ops - Export schedule timeline]] — `GET /api/{cloudId}/v1/schedules/{scheduleId}.ics` — Export schedule timeline 📎

## Syncs

- [[JSM Ops - List syncs]] — `GET /api/{cloudId}/v1/syncs` — List syncs
- [[JSM Ops - Create sync]] — `POST /api/{cloudId}/v1/syncs` — Create sync ✏️
- [[JSM Ops - Get sync]] — `GET /api/{cloudId}/v1/syncs/{id}` — Get sync
- [[JSM Ops - Delete sync]] — `DELETE /api/{cloudId}/v1/syncs/{id}` — Delete sync ✏️
- [[JSM Ops - Update sync]] — `PATCH /api/{cloudId}/v1/syncs/{id}` — Update sync ✏️

## Sync actions

- [[JSM Ops - List sync actions]] — `GET /api/{cloudId}/v1/syncs/{syncId}/actions` — List sync actions
- [[JSM Ops - Create sync action]] — `POST /api/{cloudId}/v1/syncs/{syncId}/actions` — Create sync action ✏️
- [[JSM Ops - Get sync action]] — `GET /api/{cloudId}/v1/syncs/{syncId}/actions/{id}` — Get sync action
- [[JSM Ops - Delete sync action]] — `DELETE /api/{cloudId}/v1/syncs/{syncId}/actions/{id}` — Delete sync action ✏️
- [[JSM Ops - Update sync action]] — `PATCH /api/{cloudId}/v1/syncs/{syncId}/actions/{id}` — Update sync action ✏️
- [[JSM Ops - Reorder sync action]] — `PATCH /api/{cloudId}/v1/syncs/{syncId}/actions/{id}/order` — Reorder sync action ✏️

## Sync action groups

- [[JSM Ops - List sync action groups]] — `GET /api/{cloudId}/v1/syncs/{syncId}/action-groups` — List sync action groups
- [[JSM Ops - Create sync action group]] — `POST /api/{cloudId}/v1/syncs/{syncId}/action-groups` — Create sync action group ✏️
- [[JSM Ops - Get sync action group]] — `GET /api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}` — Get sync action group
- [[JSM Ops - Delete sync action group]] — `DELETE /api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}` — Delete sync action group ✏️
- [[JSM Ops - Update sync action group]] — `PATCH /api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}` — Update sync action group ✏️
- [[JSM Ops - Reorder sync action group]] — `PATCH /api/{cloudId}/v1/syncs/{syncId}/action-groups/{id}/order` — Reorder sync action group ✏️

## JEC

- [[JSM Ops - List JEC channels]] — `GET /api/{cloudId}/v1/jec/channels` — List JEC channels
- [[JSM Ops - Create JEC Channel]] — `POST /api/{cloudId}/v1/jec/channels` — Create JEC Channel ✏️
- [[JSM Ops - Get JEC channel]] — `GET /api/{cloudId}/v1/jec/channels/{id}` — Get JEC channel
- [[JSM Ops - Delete JEC channel]] — `DELETE /api/{cloudId}/v1/jec/channels/{id}` — Delete JEC channel ✏️
- [[JSM Ops - Send JEC Action]] — `POST /api/{cloudId}/v1/jec/action` — Send JEC Action ✏️

## Status Page

- [[JSM Ops - Get page by ID]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}` — Get page by ID
- [[JSM Ops - Update page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/update` — Update page ✏️
- [[JSM Ops - Soft delete page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/soft_delete` — Soft delete page ✏️
- [[JSM Ops - Create page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages` — Create page ✏️
- [[JSM Ops - Permanently delete page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/permanent_delete` — Permanently delete page ✏️
- [[JSM Ops - Delete page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/delete` — Delete page ✏️
- [[JSM Ops - Delete page permanently (alias)]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/delete_permanently` — Delete page permanently (alias) ✏️
- [[JSM Ops - Recover page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/recover` — Recover page ✏️
- [[JSM Ops - Recover deleted page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/recover_deleted` — Recover deleted page ✏️
- [[JSM Ops - Unpublish page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/unpublish` — Unpublish page ✏️
- [[JSM Ops - Get page summary details]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/summary` — Get page summary details
- [[JSM Ops - Get page uptime percentage]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/uptime_percentage` — Get page uptime percentage
- [[JSM Ops - Get page by name]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/by_name/{name}` — Get page by name
- [[JSM Ops - Check if Status page name is unique]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/validate/name/{name}` — Check if Status page name is unique
- [[JSM Ops - Get unique subdomain suggestion]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/subdomain/suggest/{pageName}` — Get unique subdomain suggestion
- [[JSM Ops - Check if subdomain is available]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/subdomain/validate/{subdomain}` — Check if subdomain is available
- [[JSM Ops - Get pages summary by cloud ID]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/summary` — Get pages summary by cloud ID
- [[JSM Ops - Get pages summary by cloud ID V2]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/summary/v2` — Get pages summary by cloud ID V2
- [[JSM Ops - Create draft page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/draft` — Create draft page ✏️
- [[JSM Ops - Get draft page by ID]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{pageId}` — Get draft page by ID
- [[JSM Ops - Update draft page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{draftPageId}/update` — Update draft page ✏️
- [[JSM Ops - Delete draft page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{draftPageId}/delete` — Delete draft page ✏️
- [[JSM Ops - Get draft page by name]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/by_name/{name}` — Get draft page by name
- [[JSM Ops - Publish draft page]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/pages/draft/{draftPageId}/publish` — Publish draft page ✏️
- [[JSM Ops - Batch process draft components]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/components/batch_process` — Batch process draft components ✏️
- [[JSM Ops - List components in draft for a status page]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/draft` — List components in draft for a status page.
- [[JSM Ops - Get components uptime for page]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/uptime` — Get components uptime for page
- [[JSM Ops - Get a paginated list of components in draft for the status page]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/draft/v2` — Get a paginated list of components in draft for the status page
- [[JSM Ops - Get components uptime for page with pagination]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/pages/{pageId}/components/uptime/v2` — Get components uptime for page with pagination
- [[JSM Ops - Get component with uptime]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/components/{componentId}/uptime` — Get component with uptime
- [[JSM Ops - Get component uptime percentage]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/components/{componentId}/uptime_percentage` — Get component uptime percentage
- [[JSM Ops - List incidents]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/list` — List incidents
- [[JSM Ops - Create incident]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/incidents` — Create incident ✏️
- [[JSM Ops - Update incident]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/incidents/update` — Update incident ✏️
- [[JSM Ops - List incident templates]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/templates/list` — List incident templates
- [[JSM Ops - Get incident template]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/templates/{incidentTemplateId}` — Get incident template
- [[JSM Ops - Get incident by various identifiers]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/get` — Get incident by various identifiers
- [[JSM Ops - List incidents with pagination]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/incidents/list/v2` — List incidents with pagination
- [[JSM Ops - List subscribers]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/list` — List subscribers
- [[JSM Ops - Create subscriber]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/subscribers` — Create subscriber ✏️
- [[JSM Ops - Unsubscribe]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/subscribers/unsubscribe` — Unsubscribe ✏️
- [[JSM Ops - Validate subscriber token]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/subscribers/validate_token` — Validate subscriber token
- [[JSM Ops - Get total subscribers in cloud]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/total_in_cloud` — Get total subscribers in cloud
- [[JSM Ops - Get subscription stats]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/stats` — Get subscription stats
- [[JSM Ops - List subscribers with pagination and filters]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/subscribers/list/connection` — List subscribers with pagination and filters
- [[JSM Ops - Delete subscribers]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/subscribers/delete` — Delete subscribers ✏️

## Stakeholder User management

- [[JSM Ops - List stakeholders]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/list` — List stakeholders
- [[JSM Ops - Create stakeholder]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders` — Create stakeholder ✏️
- [[JSM Ops - Update stakeholder]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/update` — Update stakeholder ✏️
- [[JSM Ops - Delete stakeholder]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/{stakeholderId}/delete` — Delete stakeholder ✏️
- [[JSM Ops - Bulk create stakeholders]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/bulk` — Bulk create stakeholders ✏️
- [[JSM Ops - Bulk delete stakeholders]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/bulk_delete` — Bulk delete stakeholders ✏️
- [[JSM Ops - Resend stakeholder invite]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/resend_invite` — Resend stakeholder invite ✏️
- [[JSM Ops - Get stakeholder by various identifiers]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/get` — Get stakeholder by various identifiers
- [[JSM Ops - Get stakeholders by ARI list]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/by_ari` — Get stakeholders by ARI list
- [[JSM Ops - Get stakeholders by assignment with pagination]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/by_assignment/v2` — Get stakeholders by assignment with pagination
- [[JSM Ops - Get flattened stakeholders list]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/flattened_list` — Get flattened stakeholders list
- [[JSM Ops - Get stakeholders from similar incidents]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/from_similar_incidents/{incidentKey}` — Get stakeholders from similar incidents
- [[JSM Ops - Remove stakeholder assignment]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholders/assignments/remove` — Remove stakeholder assignment ✏️
- [[JSM Ops - Create stakeholder group]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups` — Create stakeholder group ✏️
- [[JSM Ops - Get stakeholder group by ID]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}` — Get stakeholder group by ID
- [[JSM Ops - Update stakeholder group]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/update` — Update stakeholder group ✏️
- [[JSM Ops - Delete stakeholder group]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/delete` — Delete stakeholder group ✏️
- [[JSM Ops - Add members to stakeholder group]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/members` — Add members to stakeholder group ✏️
- [[JSM Ops - Remove members from stakeholder group]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/members/remove` — Remove members from stakeholder group ✏️
- [[JSM Ops - Get stakeholder groups by membership]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/by_membership/{id}` — Get stakeholder groups by membership
- [[JSM Ops - Get stakeholder group with memberships]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{id}/with_memberships` — Get stakeholder group with memberships
- [[JSM Ops - Get stakeholder groups with memberships]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/with_memberships` — Get stakeholder groups with memberships
- [[JSM Ops - Get stakeholder groups with stakeholders]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/with_stakeholders` — Get stakeholder groups with stakeholders
- [[JSM Ops - Get stakeholder groups by name]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/by_name/{name}` — Get stakeholder groups by name
- [[JSM Ops - Get memberships by group ID]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/{groupId}/memberships` — Get memberships by group ID
- [[JSM Ops - Check if stakeholder group name is unique]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/validate/name/{name}` — Check if stakeholder group name is unique
- [[JSM Ops - Remove multiple stakeholder groups]] — `POST /stakeholder-comms/cloudId/{cloudId}/api/stakeholder_groups/bulk_delete` — Remove multiple stakeholder groups ✏️
- [[JSM Ops - Get assignments by stakeholder with pagination]] — `GET /stakeholder-comms/cloudId/{cloudId}/api/assignments/by_stakeholder/v2` — Get assignments by stakeholder with pagination
