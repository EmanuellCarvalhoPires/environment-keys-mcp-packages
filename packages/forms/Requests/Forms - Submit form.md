---
tags:
  - api/request
  - api/service/atlassian
  - api/app/forms
  - api/resource/forms-on-customer-request
  - api/operation/update
  - api/effect/write
up: "[[MCP - Forms]]"
app: "Forms"
method: PUT
path: "/request/{issueIdOrKey}/form/{formId}/action/submit"
category: "Forms on Customer Request"
writes_data: true
---
# Forms - Submit form

**Submit form** — `PUT /request/{issueIdOrKey}/form/{formId}/action/submit`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"Forms - Submit form"`.
- Official documentation: https://developer.atlassian.com/cloud/forms/rest/

```http
PUT https://api.atlassian.com/jira/forms/cloud/{{service.cloud_id}}/request/{{param:issueIdOrKey}}/form/{{param:formId}}/action/submit
Authorization: {{service.auth_token}}
Accept: application/json
```

## Parameters

- `issueIdOrKey` (path, string, required) — The issue key or ID
- `formId` (path, string, required) — The ID of the form

## Original description

Changes the status of a form on a request to submitted.Depending on how the form is configured the form may either enter the submitted state or the locked state. Locked forms are considered to be submitted and locked and can only be reopened by project admins.We validate form answers before submission. This includes built-in rules and rules configured by Jira admins.

**[Permissions](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/#permissions) required:**

 *  *Edit request* permission to edit the customer request.
