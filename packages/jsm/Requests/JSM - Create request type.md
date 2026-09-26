---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/servicedesk
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype"
category: "Servicedesk"
writes_data: true
tool_note: "[[jsm_create_request_type]]"
---
# JSM - Create request type

**Create request type** — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype`

- Run by the tool [[jsm_create_request_type]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/servicedesk/{{param:serviceDeskId}}/requesttype
Authorization: {{service.auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `serviceDeskId` (path, string, required) — The ID of the service desk where the customer request type is to be created. This can alternatively be a project identifier.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "description": "Get IT Help",
  "helpText": "Please tell us clearly the problem you have within 100 words.",
  "issueTypeId": "12345",
  "name": "Get IT Help"
}
```

## Original description

This method enables a customer request type to be added to a service desk based on an issue type. Note that not all customer request type fields can be specified in the request and these fields are given the following default values:

 *  Request type icon is given the headset icon.
 *  Request type groups is left empty, which means this customer request type will not be visible on the [customer portal](https://confluence.atlassian.com/servicedeskcloud/configuring-the-customer-portal-732528918.html).
 *  Request type status mapping is left empty, so the request type has no custom status mapping but inherits the status map from the issue type upon which it is based.
 *  Request type field mapping is set to show the required fields as specified by the issue type used to create the customer request type.

  
These fields can be updated by a service desk administrator using the **Request types** option in **Project settings**.  
Request Types are created in next-gen projects by creating Issue Types. Please use the Jira Cloud Platform Create issue type endpoint instead.

**[Permissions](#permissions) required**: Service desk's administrator
