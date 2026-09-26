---
tags:
  - moc
  - mcp
  - api/app/forms
up: "[[MCP Tools]]"
---
# MCP - Forms

- **Tools:** 0 (exposed: 0; the others via `run_vault_tool`)
- **Requests only:** 34
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/forms/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Forms Export

- [[Forms - Start export]] — `POST /export` — Start export ✏️
- [[Forms - Get export status]] — `GET /export/{exportId}` — Get export status
- [[Forms - Download export result]] — `GET /export/{exportId}/{filename}` — Download export result 📎

## Forms on Customer Request

- [[Forms - Get form index]] — `GET /request/{issueIdOrKey}/form` — Get form index
- [[Forms - Get form]] — `GET /request/{issueIdOrKey}/form/{formId}` — Get form
- [[Forms - Save form answers]] — `PUT /request/{issueIdOrKey}/form/{formId}` — Save form answers ✏️
- [[Forms - Submit form]] — `PUT /request/{issueIdOrKey}/form/{formId}/action/submit` — Submit form ✏️
- [[Forms - Get form attachments metadata]] — `GET /request/{issueIdOrKey}/form/{formId}/attachment` — Get form attachments metadata
- [[Forms - Get external form data]] — `GET /request/{issueIdOrKey}/form/{formId}/externaldata` — Get external form data
- [[Forms - Get form simplified answers]] — `GET /request/{issueIdOrKey}/form/{formId}/format/answers` — Get form simplified answers
- [[Forms - Get form PDF]] — `GET /request/{issueIdOrKey}/form/{formId}/format/pdf` — Get form PDF 📎
- [[Forms - Get form XLSX]] — `GET /request/{issueIdOrKey}/form/{formId}/format/xlsx` — Get form XLSX 📎

## Forms on Issue

- [[Forms - Get form index (GET)]] — `GET /issue/{issueIdOrKey}/form` — Get form index
- [[Forms - Add form]] — `POST /issue/{issueIdOrKey}/form` — Add form ✏️
- [[Forms - Get form (GET)]] — `GET /issue/{issueIdOrKey}/form/{formId}` — Get form
- [[Forms - Save form answers (PUT)]] — `PUT /issue/{issueIdOrKey}/form/{formId}` — Save form answers ✏️
- [[Forms - Delete form]] — `DELETE /issue/{issueIdOrKey}/form/{formId}` — Delete form ✏️
- [[Forms - Change visibility to external]] — `PUT /issue/{issueIdOrKey}/form/{formId}/action/external` — Change visibility to external ✏️
- [[Forms - Change visibility to internal]] — `PUT /issue/{issueIdOrKey}/form/{formId}/action/internal` — Change visibility to internal ✏️
- [[Forms - Reopen form]] — `PUT /issue/{issueIdOrKey}/form/{formId}/action/reopen` — Reopen form ✏️
- [[Forms - Submit form (PUT)]] — `PUT /issue/{issueIdOrKey}/form/{formId}/action/submit` — Submit form ✏️
- [[Forms - Get form attachments metadata (GET)]] — `GET /issue/{issueIdOrKey}/form/{formId}/attachment` — Get form attachments metadata
- [[Forms - Get external form data (GET)]] — `GET /issue/{issueIdOrKey}/form/{formId}/externaldata` — Get external form data
- [[Forms - Get form simplified answers (GET)]] — `GET /issue/{issueIdOrKey}/form/{formId}/format/answers` — Get form simplified answers
- [[Forms - Get form PDF (GET)]] — `GET /issue/{issueIdOrKey}/form/{formId}/format/pdf` — Get form PDF 📎
- [[Forms - Get form XLSX (GET)]] — `GET /issue/{issueIdOrKey}/form/{formId}/format/xlsx` — Get form XLSX 📎
- [[Forms - Copy forms]] — `POST /issue/{sourceIssueIdOrKey}/form/copy/{targetIssueIdOrKey}` — Copy forms ✏️

## Forms on Portal

- [[Forms - Get form on a request type]] — `GET /servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/form` — Get form on a request type
- [[Forms - Get external form data on a request type]] — `GET /servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/form/externaldata` — Get external form data on a request type

## Forms on Project

- [[Forms - Get project form index]] — `GET /project/{projectIdOrKey}/form` — Get project form index
- [[Forms - Create form template]] — `POST /project/{projectIdOrKey}/form` — Create form template ✏️
- [[Forms - Get form template]] — `GET /project/{projectIdOrKey}/form/{formId}` — Get form template
- [[Forms - Save form template]] — `PUT /project/{projectIdOrKey}/form/{formId}` — Save form template ✏️
- [[Forms - Delete form template]] — `DELETE /project/{projectIdOrKey}/form/{formId}` — Delete form template ✏️
