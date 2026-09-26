---
tags:
  - api/request
  - api/service/atlassian
  - api/app/assets
  - api/resource/importsource
  - api/operation/update
  - api/effect/write
up: "[[MCP - Assets]]"
app: "Assets"
method: PUT
path: "/importsource/{importSourceId}/mapping"
category: "Importsource"
writes_data: true
tool_note: "[[assets_update_importsource_mapping]]"
---
# Assets - PUT importsource {importSourceId} mapping

**/importsource/{importSourceId}/mapping** — `PUT /importsource/{importSourceId}/mapping`

- Run by the tool [[assets_update_importsource_mapping]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PUT https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/mapping
Authorization: {{service.auth_token}}
Content-Type: application/json

{{param:body}}
```

## Parameters

- `importSourceId` (path, string, required) — Value of importSourceId in the path.
- `body` (body, object, required) — JSON request body. See the example in the request note.

## Body (example)

```json
{
  "schema": {
    "objectSchema": {
      "name": "Disk Analysis Tool",
      "description": "Data imported from The Disk Analysis Tool",
      "objectTypes": [
        {
          "externalId": "object-type/hard-drive",
          "name": "Hard Drive",
          "description": "A hard drive found during scanning",
          "attributes": [
            {
              "externalId": "object-type-attribute/duid",
              "name": "DUID",
              "description": "Device Unique Identifier",
              "type": "text",
              "label": true,
              "minimumCardinality": 1,
              "maximumCardinality": 1,
              "unique": false
            },
            {
              "externalId": "object-type-attribute/disk-label",
              "name": "Disk Label",
              "description": "Hard drive label",
              "type": "text",
              "minimumCardinality": 1,
              "maximumCardinality": 1,
              "unique": false
            },
            {
              "externalId": "object-type-attribute/status",
              "name": "HardDriveStatus",
              "description": "The hard drive status",
              "type": "status",
              "typeValues": [
                "Schema Scope Status",
                "Global Scope Status",
                "New Status"
              ]
            }
          ],
          "children": [
            {
              "externalId": "object-type/file",
              "name": "File",
              "description": "A file present in a hard drive",
              "attributes": [
                {
                  "externalId": "object-type-attribute/path",
                  "name": "Path",
                  "description": "Path of the file",
                  "type": "text",
                  "label": true,
                  "minimumCardinality": 1,
                  "maximumCardinality": 1,
                  "unique": false
                },
                {
                  "externalId": "object-type-attribute/size",
                  "name": "Size",
                  "description": "Size of the file",
                  "type": "integer",
                  "minimumCardinality": 1,
                  "maximumCardinality": 1,
                  "unique": false
                }
              ]
            }
          ]
        }
      ]
    },
    "statusSchema": {
      "statuses": [
        {
          "name": "New Status",
          "description": "",
          "category": "active"
        }
      ]
    }
  },
  "mapping": {
    "objectTypeMappings": [
      {
        "objectTypeExternalId": "object-type/hard-drive",
        "objectTypeName": "Hard Drive",
        "selector": "hardDrives",
        "description": "Mapping for Hard Drives",
        "attributesMapping": [
          {
            "attributeExternalId": "object-type-attribute/duid",
            "attributeName": "DUID",
            "attributeLocators": [
              "id"
            ],
            "externalIdPart": true
          },
          {
            "attributeExternalId": "object-type-attribute/disk-label",
            "attributeName": "Disk Label",
            "attributeLocators": [
              "label"
            ]
          },
          {
            "attributeExternalId": "object-type-attribute/status",
            "attributeName": "HardDriveStatus",
            "attributeLocators": [
              "status"
            ]
          }
        ]
      },
      {
        "objectTypeExternalId": "object-type/file",
        "objectTypeName": "File",
        "selector": "hardDrives.files",
        "description": "Maps files found in hard drives",
        "attributesMapping": [
          {
            "attributeExternalId": "object-type-attribute/path",
            "attributeName": "Path",
            "attributeLocators": [
              "path"
            ],
            "externalIdPart": true
          },
          {
            "attributeExternalId": "object-type-attribute/size",
            "attributeName": "Size",
            "attributeLocators": [
              "size"
            ]
          }
        ]
      }
    ]
  }
}
```

## Original description

Provide object schema and mapping configuration for the external import
