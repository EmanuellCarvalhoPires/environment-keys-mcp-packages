---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jira
  - api/resource/projects
  - api/operation/create
  - api/effect/write
  - api/permission/global-admin
up: "[[MCP - Jira v3]]"
app: "Jira v3"
method: POST
path: "/rest/api/3/project"
category: "Projects"
writes_data: true
tool_note: "[[jira_create_project]]"
---
# Jira v3 - Create project

**Create project** — `POST /rest/api/3/project`

- Run by the tool [[jira_create_project]].
- Official documentation: https://developer.atlassian.com/cloud/jira/platform/rest/v3/

```http
POST {{service.url}}/rest/api/3/project
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "assigneeType": "PROJECT_LEAD",
  "avatarId": 10200,
  "categoryId": 10120,
  "description": "Cloud migration initiative",
  "issueSecurityScheme": 10001,
  "key": "EX",
  "leadAccountId": "5b10a0effa615349cb016cd8",
  "name": "Example",
  "notificationScheme": 10021,
  "permissionScheme": 10011,
  "projectTemplateKey": "com.atlassian.jira-core-project-templates:jira-core-simplified-process-control",
  "projectTypeKey": "business",
  "url": "http://atlassian.com"
}
```

## Original description

Creates a project based on a project type template, as shown in the following table:

| Project Type Key | Project Template Key |  
|--|--|  
| `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`, `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` |  
| `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`, `com.atlassian.servicedesk:simplified-external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`, `com.atlassian.servicedesk:simplified-facilities-service-desk`, `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`, `com.atlassian.servicedesk:simplified-design-service-desk`, `com.atlassian.servicedesk:simplified-sales-service-desk`, `com.atlassian.servicedesk:simplified-finance-service-desk`, `com.atlassian.servicedesk:company-managed-blank-service-project`, `com.atlassian.servicedesk:company-managed-general-service-project`, `com.atlassian.servicedesk:team-managed-general-service-project`, `com.atlassian.servicedesk:next-gen-it-service-desk`, `com.atlassian.servicedesk:next-gen-hr-service-desk`, `com.atlassian.servicedesk:next-gen-legal-service-desk`, `com.atlassian.servicedesk:next-gen-marketing-service-desk`, `com.atlassian.servicedesk:next-gen-facilities-service-desk`, `com.atlassian.servicedesk:next-gen-analytics-service-desk`, `com.atlassian.servicedesk:next-gen-finance-service-desk`, `com.atlassian.servicedesk:next-gen-design-service-desk`, `com.atlassian.servicedesk:next-gen-sales-service-desk` |  
| `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`, `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-simplified-scrum-classic` |  
| `customer_service` | `com.atlassian.jcs:customer-service-management` |  
The project types are available according to the installed Jira features as follows:

 *  Jira Core, the default, enables `business` projects.
 *  Jira Service Management enables `service_desk` projects.
 *  Jira Software enables `software` projects.
 *  Jira Customer Service enables `customer_service` projects.

To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance, use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-ons](https://confluence.atlassian.com/x/S31NLg).

**[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
