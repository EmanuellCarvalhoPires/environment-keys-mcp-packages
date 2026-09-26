---
tags:
  - api/request
  - api/service/atlassian
  - api/app/jsm
  - api/resource/request
  - api/operation/create
  - api/effect/write
up: "[[MCP - JSM]]"
app: "JSM"
method: POST
path: "/rest/servicedeskapi/request"
category: "Request"
writes_data: true
tool_note: "[[jsm_create_customer_request]]"
---
# JSM - Create customer request

**Create customer request** — `POST /rest/servicedeskapi/request`

- Run by the tool [[jsm_create_customer_request]].
- Official documentation: https://developer.atlassian.com/cloud/jira/service-desk/rest/

```http
POST {{service.url}}/rest/servicedeskapi/request
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "form": {
    "answers": {
      "1": {
        "text": "Answer to a text form field"
      },
      "2": {
        "date": "2023-07-06"
      },
      "3": {
        "time": "14:35"
      },
      "4": {
        "choices": [
          "5"
        ]
      },
      "5": {
        "users": [
          "qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d69abfa3980ce712caae"
        ]
      }
    }
  },
  "isAdfRequest": false,
  "requestFieldValues": {
    "description": "I need a new *mouse* for my Mac",
    "summary": "Request JSD help via REST"
  },
  "requestParticipants": [
    "qm:a713c8ea-1075-4e30-9d96-891a7d181739:5ad6d69abfa3980ce712caae"
  ],
  "requestTypeId": "25",
  "serviceDeskId": "10"
}
```

## Original description

This method creates a customer request in a service desk.

The JSON request must include the service desk and customer request type, as well as any fields that are required for the request type. A list of the fields required by a customer request type can be obtained using [servicedesk/\{serviceDeskId\}/requesttype/\{requestTypeId\}/field](#api-servicedesk-serviceDeskId-requesttype-requestTypeId-field-get).

The fields required for a customer request type depend on the user's permissions:

 *  `raiseOnBehalfOf` is not available to Users who have the customer permission only.
 *  `requestParticipants` is not available to Users who have the customer permission only or if the feature is turned off for customers.

`requestFieldValues` is a map of Jira field IDs and their values. See [Field input formats](#fieldformats), for details of each field's JSON semantics and the values they can take.

**[Permissions](#permissions) required**: Permission to create requests in the specified service desk.
