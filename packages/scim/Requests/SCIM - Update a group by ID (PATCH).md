---
tags:
  - api/request
  - api/service/atlassian
  - api/app/scim
  - api/resource/groups
  - api/operation/update
  - api/effect/write
up: "[[MCP - SCIM]]"
app: "SCIM"
method: PATCH
path: "/scim/directory/{directoryId}/Groups/{id}"
category: "Groups"
writes_data: true
---
# SCIM - Update a group by ID (PATCH)

**Update a group by ID (PATCH)** — `PATCH /scim/directory/{directoryId}/Groups/{id}`

- No dedicated tool: run it with `atlassian_request_write` passing `request:"SCIM - Update a group by ID (PATCH)"`.
- Official documentation: https://developer.atlassian.com/cloud/admin/user-provisioning/rest/

```http
PATCH https://api.atlassian.com/scim/directory/{{param:directoryId}}/Groups/{{param:id}}
Authorization: {{service.scim_auth_token}}
Accept: application/json
Content-Type: application/json

{{param:body}}
```

## Parameters

- `directoryId` (path, string, required) — The SCIM base URL that is generated when conecting an identity provider with SCIM provisioning.
- `id` (path, string, required) — Unique SCIM id that serves as reference to the group. Use the Get groups API to get the SCIM id.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Original description

Updates a group's information in the directory and manages group membership.

**Note:** Renaming groups after they've synced to your Atlassian organization isn't supported in this 
release of User Provisioning API. To rename a group, create a new group with the desired 
name, update membership, and then delete the old group.

#### Example

Some HTTP headers omitted and JSON payloads formatted for readability.

```
# Request
PATCH /scim/directory/2fb21891-7bee-4c2d-a61a-ade3834c8b2b/Groups/50202593-bc47-45df-8fa0-3f63343aa3c1 HTTP/1.1
Accept: application/scim+json
Accept-Charset: utf-8
Content-Type: application/scim+json; charset=utf-8
Authorization: Bearer 0j6lDgrjU7HmGagocgLe
Host: api.atlassian.com

{
   "schemas":[
      "urn:ietf:params:scim:api:messages:2.0:PatchOp"
   ],
   "Operations":[
      {
         "op":"add",
         "path":"members",
         "value":[
            {
               "value":"c6993c94-dbda-40f1-b6f0-18c855522ade",
               "display":"dave.meyer@demotime.authteam.com"
            },
            {
               "value":"f0ae48f7-1466-445e-85ea-e83ef754aefd",
               "display":"lingbo.lu@demotime.authteam.com"
            },
            {
               "value":"432d6f10-2e28-454e-be99-0f8c732a046f",
               "display":"joanna@demotime.authteam.com"
            }
         ]
      }
   ]
}

# Response
HTTP/1.1 200
Content-Type: application/scim+json

{
   "schemas":[
      "urn:ietf:params:scim:schemas:core:2.0:Group"
   ],
   "id":"50202593-bc47-45df-8fa0-3f63343aa3c1",
   "displayName":"demotime-confluence-users",
   "members":[
      {
         "type":"User",
         "value":"f0ae48f7-1466-445e-85ea-e83ef754aefd",
         "display":"lingbo.lu@demotime.authteam.com",
         "$ref":"https://api.atlassian.com/scim/directory/2fb21891-7bee-4c2d-a61a-ade3834c8b2b/Users/f0ae48f7-1466-445e-85ea-e83ef754aefd"
      },
      {
         "type":"User",
         "value":"c6993c94-dbda-40f1-b6f0-18c855522ade",
         "display":"dave.meyer@demotime.authteam.com",
         "$ref":"https://api.atlassian.com/scim/directory/2fb21891-7bee-4c2d-a61a-ade3834c8b2b/Users/c6993c94-dbda-40f1-b6f0-18c855522ade"
      },
      {
         "type":"User",
         "value":"432d6f10-2e28-454e-be99-0f8c732a046f",
         "display":"joanna@demotime.authteam.com",
         "$ref":"https://api.atlassian.com/scim/directory/2fb21891-7bee-4c2d-a61a-ade3834c8b2b/Users/432d6f10-2e28-454e-be99-0f8c732a046f"
      }
   ],
   "meta":{
      "resourceType":"Group",
      "location":"https://api.atlassian.com/scim/directory/2fb21891-7bee-4c2d-a61a-ade3834c8b2b/Groups/50202593-bc47-45df-8fa0-3f63343aa3c1",
      "lastModified":"2018-09-26T17:49:09.420654Z",
      "created":"2018-09-26T17:41:35.49073Z"
   }
}
```
