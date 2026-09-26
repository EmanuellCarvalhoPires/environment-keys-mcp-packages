---
tags:
  - moc
  - mcp
  - api/app/assets
up: "[[MCP Tools]]"
---
# MCP - Assets

- **Tools:** 60 (exposed: 5; the others via `run_vault_tool`)
- **Requests only:** 1
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/assets/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Icon

- [[assets_get_icon]] — `GET /icon/{id}` — /icon/{id}
- [[Assets - GET icon {id} icon.png]] — `GET /icon/{id}/icon.png` — /icon/{id}/icon.png 📎
- [[assets_get_icon_global]] — `GET /icon/global` — /icon/global

## Import

- [[assets_post_import_start]] — `POST /import/start/{id}` — /import/start/{id} ✏️

## Importsource

- [[assets_get_import_source_by_id]] — `GET /importsource/{id}` — Get import source by ID
- [[assets_update_importsource_mapping]] — `PUT /importsource/{importSourceId}/mapping` — /importsource/{importSourceId}/mapping ✏️
- [[assets_patch_importsource_mapping]] — `PATCH /importsource/{importSourceId}/mapping` — /importsource/{importSourceId}/mapping ✏️
- [[assets_get_importsource_mapping_progress]] — `GET /importsource/{importSourceId}/mapping/progress/{resourceId}` — /importsource/{importSourceId}/mapping/progress/{resourceId}
- [[assets_get_importsource_configstatus]] — `GET /importsource/{importSourceId}/configstatus` — /importsource/{importSourceId}/configstatus
- [[assets_get_importsource_schema_and_mapping]] — `GET /importsource/{importSourceId}/schema-and-mapping` — /importsource/{importSourceId}/schema-and-mapping
- [[assets_post_importsource_executions]] — `POST /importsource/{importSourceId}/executions` — /importsource/{importSourceId}/executions ✏️
- [[assets_delete_importsource_executions]] — `DELETE /importsource/{importSourceId}/executions/{importExecutionId}` — /importsource/{importSourceId}/executions/{importExecutionId} ✏️
- [[assets_update_importsource_executions_progress]] — `PUT /importsource/{importSourceId}/executions/{importExecutionId}/progress` — /importsource/{importSourceId}/executions/{importExecutionId}/progress ✏️
- [[assets_post_importsource_executions_data]] — `POST /importsource/{importSourceId}/executions/{importExecutionId}/data` — /importsource/{importSourceId}/executions/{importExecutionId}/data ✏️
- [[assets_get_importsource_executions_status]] — `GET /importsource/{importSourceId}/executions/{importExecutionId}/status` — /importsource/{importSourceId}/executions/{importExecutionId}/status
- [[assets_get_importsource_executions_status_get]] — `GET /importsource/{importSourceId}/executions/status` — /importsource/{importSourceId}/executions/status
- [[assets_post_importsource_executions_history_failed]] — `POST /importsource/{importSourceId}/executions/{executionId}/history/failed` — /importsource/{importSourceId}/executions/{executionId}/history/failed ✏️
- [[assets_post_importsource_token]] — `POST /importsource/{importSourceId}/token` — /importsource/{importSourceId}/token ✏️
- [[assets_get_importsource_schedule]] — `GET /importsource/{importSourceId}/schedule` — /importsource/{importSourceId}/schedule
- [[assets_create_import_schedule]] — `POST /importsource/{importSourceId}/importschedule` — Create import schedule ✏️
- [[assets_get_import_schedule]] — `GET /importsource/{importSourceId}/importschedule/{importScheduleId}` — Get import schedule
- [[assets_update_import_schedule]] — `PUT /importsource/{importSourceId}/importschedule/{importScheduleId}` — Update import schedule ✏️
- [[assets_delete_import_schedule]] — `DELETE /importsource/{importSourceId}/importschedule/{importScheduleId}` — Delete import schedule ✏️

## Object

- [[assets_get_object]] — `GET /object/{id}` — /object/{id} ⭐
- [[assets_update_object]] — `PUT /object/{id}` — /object/{id} ✏️
- [[assets_delete_object]] — `DELETE /object/{id}` — /object/{id} ✏️
- [[assets_get_object_attributes]] — `GET /object/{id}/attributes` — /object/{id}/attributes
- [[assets_get_object_history]] — `GET /object/{id}/history` — /object/{id}/history
- [[assets_get_object_referenceinfo]] — `GET /object/{id}/referenceinfo` — /object/{id}/referenceinfo
- [[assets_post_object_create]] — `POST /object/create` — /object/create ✏️⭐
- [[assets_post_object_navlist_aql]] — `POST /object/navlist/aql` — /object/navlist/aql
- [[assets_post_object_aql]] — `POST /object/aql` — /object/aql ⭐
- [[assets_post_object_aql_totalcount]] — `POST /object/aql/totalcount` — /object/aql/totalcount

## Objectconnectedtickets

- [[assets_get_objectconnectedtickets_tickets]] — `GET /objectconnectedtickets/{objectId}/tickets` — /objectconnectedtickets/{objectId}/tickets

## Objectschema

- [[assets_get_objectschema_list]] — `GET /objectschema/list` — /objectschema/list ⭐
- [[assets_post_objectschema_create]] — `POST /objectschema/create` — /objectschema/create ✏️
- [[assets_get_objectschema]] — `GET /objectschema/{id}` — /objectschema/{id}
- [[assets_update_objectschema]] — `PUT /objectschema/{id}` — /objectschema/{id} ✏️
- [[assets_delete_objectschema]] — `DELETE /objectschema/{id}` — /objectschema/{id} ✏️
- [[assets_get_objectschema_attributes]] — `GET /objectschema/{id}/attributes` — /objectschema/{id}/attributes
- [[assets_get_objectschema_objecttypes]] — `GET /objectschema/{id}/objecttypes` — /objectschema/{id}/objecttypes
- [[assets_get_objectschema_objecttypes_flat]] — `GET /objectschema/{id}/objecttypes/flat` — /objectschema/{id}/objecttypes/flat ⭐

## Objecttype

- [[assets_get_objecttype]] — `GET /objecttype/{id}` — /objecttype/{id}
- [[assets_update_objecttype]] — `PUT /objecttype/{id}` — /objecttype/{id} ✏️
- [[assets_delete_objecttype]] — `DELETE /objecttype/{id}` — /objecttype/{id} ✏️
- [[assets_get_objecttype_attributes]] — `GET /objecttype/{id}/attributes` — /objecttype/{id}/attributes
- [[assets_post_objecttype_position]] — `POST /objecttype/{id}/position` — /objecttype/{id}/position ✏️
- [[assets_post_objecttype_create]] — `POST /objecttype/create` — /objecttype/create ✏️

## Objecttypeattribute

- [[assets_post_objecttypeattribute]] — `POST /objecttypeattribute/{objectTypeId}` — /objecttypeattribute/{objectTypeId} ✏️
- [[assets_update_objecttypeattribute]] — `PUT /objecttypeattribute/{objectTypeId}/{id}` — /objecttypeattribute/{objectTypeId}/{id} ✏️
- [[assets_delete_objecttypeattribute]] — `DELETE /objecttypeattribute/{id}` — /objecttypeattribute/{id} ✏️

## Progress

- [[assets_get_progress_category_imports]] — `GET /progress/category/imports/{id}` — /progress/category/imports/{id}

## Config

- [[assets_get_config_statustype]] — `GET /config/statustype` — /config/statustype
- [[assets_post_config_statustype]] — `POST /config/statustype` — /config/statustype ✏️
- [[assets_get_config_statustype_get]] — `GET /config/statustype/{id}` — /config/statustype/{id}
- [[assets_update_config_statustype]] — `PUT /config/statustype/{id}` — /config/statustype/{id} ✏️
- [[assets_delete_config_statustype]] — `DELETE /config/statustype/{id}` — /config/statustype/{id} ✏️
- [[assets_get_config_referencetype]] — `GET /config/referencetype` — /config/referencetype
- [[assets_post_config_referencetype]] — `POST /config/referencetype` — /config/referencetype ✏️

## Global

- [[assets_post_global_config_objectschema_property]] — `POST /global/config/objectschema/{id}/property` — /global/config/objectschema/{id}/property ✏️

## Usage

- [[assets_get_tenant_usage_information]] — `GET /usage` — Get tenant usage information
