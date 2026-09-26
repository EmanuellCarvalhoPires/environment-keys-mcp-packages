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
method: PATCH
path: "/importsource/{importSourceId}/mapping"
category: "Importsource"
writes_data: true
tool_note: "[[assets_patch_importsource_mapping]]"
---
# Assets - PATCH importsource {importSourceId} mapping

**/importsource/{importSourceId}/mapping** — `PATCH /importsource/{importSourceId}/mapping`

- Run by the tool [[assets_patch_importsource_mapping]].
- Official documentation: https://developer.atlassian.com/cloud/assets/rest/

```http
PATCH https://api.atlassian.com/ex/jira/{{service.cloud_id}}/jsm/assets/workspace/{{service.assets_workspace_id}}/v1/importsource/{{param:importSourceId}}/mapping
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
  "$schema": "https://api.stg.atlassian.com/jsm/assets/imports/external/schema/versions/2021_09_15",
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
              "externalId": "object-type-attribute/manufacturer",
              "name": "Manufacturer",
              "description": "Manufacturer name",
              "type": "text"
            }
          ],
          "children": [
            {
              "externalId": "object-type/folder",
              "name": "Folder",
              "description": "A folder present in a hard drive",
              "attributes": [
                {
                  "externalId": "object-type-attribute/folder-name",
                  "name": "Name",
                  "description": "Folder name",
                  "type": "text",
                  "label": true
                }
              ]
            },
            {
              "externalId": "object-type/file",
              "name": "File",
              "description": "A file present in a hard drive",
              "attributes": [
                {
                  "externalId": "object-type-attribute/path",
                  "name": "Path",
                  "description": "Updated description for the path attribute",
                  "type": "text",
                  "label": true
                }
              ]
            }
          ]
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
            "attributeExternalId": "object-type-attribute/manufacturer",
            "attributeName": "Manufacturer",
            "attributeLocators": [
              "manufacturer"
            ]
          }
        ]
      },
      {
        "objectTypeExternalId": "object-type/folder",
        "objectTypeName": "Folder",
        "selector": "hardDrives.folders",
        "description": "Mapping for Folder",
        "attributesMapping": [
          {
            "attributeExternalId": "object-type-attribute/folder-name",
            "attributeName": "Name",
            "attributeLocators": [
              "name"
            ],
            "externalIdPart": true
          }
        ]
      }
    ]
  }
}
```

## Original description

Update object schema and mapping configuration for the external import
