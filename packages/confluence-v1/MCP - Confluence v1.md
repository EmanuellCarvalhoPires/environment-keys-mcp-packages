---
tags:
  - moc
  - mcp
  - api/app/confluence
up: "[[MCP Tools]]"
---
# MCP - Confluence v1

- **Tools:** 121 (exposed: 1; the others via `run_vault_tool`)
- **Requests only:** 9
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/confluence/rest/v1/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Audit

- [[confluence_v1_get_audit_records]] — `GET /wiki/rest/api/audit` — Get audit records
- [[confluence_v1_create_audit_record]] — `POST /wiki/rest/api/audit` — Create audit record ✏️
- [[Confluence v1 - Export audit records]] — `GET /wiki/rest/api/audit/export` — Export audit records 📎
- [[confluence_v1_get_retention_period]] — `GET /wiki/rest/api/audit/retention` — Get retention period
- [[confluence_v1_set_retention_period]] — `PUT /wiki/rest/api/audit/retention` — Set retention period ✏️
- [[confluence_v1_get_audit_records_for_time_period]] — `GET /wiki/rest/api/audit/since` — Get audit records for time period

## Analytics

- [[confluence_v1_get_views]] — `GET /wiki/rest/api/analytics/content/{contentId}/views` — Get views
- [[confluence_v1_get_viewers]] — `GET /wiki/rest/api/analytics/content/{contentId}/viewers` — Get viewers

## Content

- [[confluence_v1_archive_pages]] — `POST /wiki/rest/api/content/archive` — Archive pages ✏️
- [[confluence_v1_publish_shared_draft]] — `PUT /wiki/rest/api/content/blueprint/instance/{draftId}` — Publish shared draft ✏️
- [[confluence_v1_publish_legacy_draft]] — `POST /wiki/rest/api/content/blueprint/instance/{draftId}` — Publish legacy draft ✏️
- [[confluence_v1_search_content_by_cql]] — `GET /wiki/rest/api/content/search` — Search content by CQL ⭐

## Content - attachments

- [[Confluence v1 - Create or update attachment]] — `PUT /wiki/rest/api/content/{id}/child/attachment` — Create or update attachment ✏️📎
- [[Confluence v1 - Create attachment]] — `POST /wiki/rest/api/content/{id}/child/attachment` — Create attachment ✏️📎
- [[confluence_v1_update_attachment_properties]] — `PUT /wiki/rest/api/content/{id}/child/attachment/{attachmentId}` — Update attachment properties ✏️
- [[Confluence v1 - Update attachment data]] — `POST /wiki/rest/api/content/{id}/child/attachment/{attachmentId}/data` — Update attachment data ✏️📎
- [[confluence_v1_get_uri_to_download_attachment]] — `GET /wiki/rest/api/content/{id}/child/attachment/{attachmentId}/download` — Get URI to download attachment

## Content body

- [[confluence_v1_asynchronously_convert_content_body]] — `POST /wiki/rest/api/contentbody/convert/async/{to}` — Asynchronously convert content body ✏️
- [[confluence_v1_get_asynchronously_converted_content_body_from_the]] — `GET /wiki/rest/api/contentbody/convert/async/{id}` — Get asynchronously converted content body from the id or the current status of the task.
- [[confluence_v1_get_asynchronous_content_body_conversion_task_resu]] — `GET /wiki/rest/api/contentbody/convert/async/bulk/tasks` — Get asynchronous content body conversion task result in bulk
- [[confluence_v1_create_asynchronous_content_body_conversion_tasks]] — `POST /wiki/rest/api/contentbody/convert/async/bulk/tasks` — Create asynchronous content body conversion tasks in bulk ✏️

## Content - children and descendants

- [[confluence_v1_move_a_page_to_a_new_location_relative_to_a_target]] — `PUT /wiki/rest/api/content/{pageId}/move/{position}/{targetId}` — Move a page to a new location relative to a target page ✏️
- [[confluence_v1_get_content_descendants]] — `GET /wiki/rest/api/content/{id}/descendant` — Get content descendants
- [[confluence_v1_get_content_descendants_by_type]] — `GET /wiki/rest/api/content/{id}/descendant/{type}` — Get content descendants by type
- [[confluence_v1_copy_page_hierarchy]] — `POST /wiki/rest/api/content/{id}/pagehierarchy/copy` — Copy page hierarchy ✏️
- [[confluence_v1_copy_single_page]] — `POST /wiki/rest/api/content/{id}/copy` — Copy single page ✏️

## Content - macro body

- [[confluence_v1_get_macro_body_by_macro_id]] — `GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}` — Get macro body by macro ID
- [[confluence_v1_get_macro_body_by_macro_id_and_convert_the_represe]] — `GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/{to}` — Get macro body by macro ID and convert the representation synchronously
- [[confluence_v1_get_macro_body_by_macro_id_and_convert_representat]] — `GET /wiki/rest/api/content/{id}/history/{version}/macro/id/{macroId}/convert/async/{to}` — Get macro body by macro ID and convert representation Asynchronously

## Content labels

- [[confluence_v1_add_labels_to_content]] — `POST /wiki/rest/api/content/{id}/label` — Add labels to content ✏️
- [[confluence_v1_remove_label_from_content_using_query_parameter]] — `DELETE /wiki/rest/api/content/{id}/label` — Remove label from content using query parameter ✏️
- [[confluence_v1_remove_label_from_content]] — `DELETE /wiki/rest/api/content/{id}/label/{label}` — Remove label from content ✏️

## Content permissions

- [[confluence_v1_check_content_permissions]] — `POST /wiki/rest/api/content/{id}/permission/check` — Check content permissions

## Content restrictions

- [[confluence_v1_get_restrictions]] — `GET /wiki/rest/api/content/{id}/restriction` — Get restrictions
- [[confluence_v1_update_restrictions]] — `PUT /wiki/rest/api/content/{id}/restriction` — Update restrictions ✏️
- [[confluence_v1_add_restrictions]] — `POST /wiki/rest/api/content/{id}/restriction` — Add restrictions ✏️
- [[confluence_v1_delete_restrictions]] — `DELETE /wiki/rest/api/content/{id}/restriction` — Delete restrictions ✏️
- [[confluence_v1_get_restrictions_by_operation]] — `GET /wiki/rest/api/content/{id}/restriction/byOperation` — Get restrictions by operation
- [[confluence_v1_get_restrictions_for_operation]] — `GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}` — Get restrictions for operation
- [[confluence_v1_get_content_restriction_status_for_group]] — `GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}` — Get content restriction status for group
- [[confluence_v1_add_group_to_content_restriction]] — `PUT /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}` — Add group to content restriction ✏️
- [[confluence_v1_remove_group_from_content_restriction]] — `DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/byGroupId/{groupId}` — Remove group from content restriction ✏️
- [[confluence_v1_get_content_restriction_status_for_user]] — `GET /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user` — Get content restriction status for user
- [[confluence_v1_add_user_to_content_restriction]] — `PUT /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user` — Add user to content restriction ✏️
- [[confluence_v1_remove_user_from_content_restriction]] — `DELETE /wiki/rest/api/content/{id}/restriction/byOperation/{operationKey}/user` — Remove user from content restriction ✏️

## Content states

- [[confluence_v1_get_content_state]] — `GET /wiki/rest/api/content/{id}/state` — Get content state
- [[confluence_v1_set_the_content_state_of_a_content_and_publishes_a]] — `PUT /wiki/rest/api/content/{id}/state` — Set the content state of a content and publishes a new version of the content. ✏️
- [[confluence_v1_removes_the_content_state_of_a_content_and_publish]] — `DELETE /wiki/rest/api/content/{id}/state` — Removes the content state of a content and publishes a new version. ✏️
- [[confluence_v1_gets_available_content_states_for_content]] — `GET /wiki/rest/api/content/{id}/state/available` — Gets available content states for content.
- [[confluence_v1_get_custom_content_states]] — `GET /wiki/rest/api/content-states` — Get Custom Content States
- [[confluence_v1_get_space_suggested_content_states]] — `GET /wiki/rest/api/space/{spaceKey}/state` — Get space suggested content states
- [[confluence_v1_get_content_state_settings_for_space]] — `GET /wiki/rest/api/space/{spaceKey}/state/settings` — Get content state settings for space
- [[confluence_v1_get_content_in_space_with_given_content_state]] — `GET /wiki/rest/api/space/{spaceKey}/state/content` — Get content in space with given content state

## Content versions

- [[confluence_v1_restore_content_version]] — `POST /wiki/rest/api/content/{id}/version` — Restore content version ✏️
- [[confluence_v1_delete_content_version]] — `DELETE /wiki/rest/api/content/{id}/version/{versionNumber}` — Delete content version ✏️

## Content watches

- [[confluence_v1_get_watches_for_page]] — `GET /wiki/rest/api/content/{id}/notification/child-created` — Get watches for page
- [[confluence_v1_get_watches_for_space]] — `GET /wiki/rest/api/content/{id}/notification/created` — Get watches for space
- [[confluence_v1_get_space_watchers]] — `GET /wiki/rest/api/space/{spaceKey}/watch` — Get space watchers
- [[confluence_v1_get_content_watch_status]] — `GET /wiki/rest/api/user/watch/content/{contentId}` — Get content watch status
- [[confluence_v1_add_content_watcher]] — `POST /wiki/rest/api/user/watch/content/{contentId}` — Add content watcher ✏️
- [[confluence_v1_remove_content_watcher]] — `DELETE /wiki/rest/api/user/watch/content/{contentId}` — Remove content watcher ✏️
- [[confluence_v1_get_label_watch_status]] — `GET /wiki/rest/api/user/watch/label/{labelName}` — Get label watch status
- [[confluence_v1_add_label_watcher]] — `POST /wiki/rest/api/user/watch/label/{labelName}` — Add label watcher ✏️
- [[confluence_v1_remove_label_watcher]] — `DELETE /wiki/rest/api/user/watch/label/{labelName}` — Remove label watcher ✏️
- [[confluence_v1_get_space_watch_status]] — `GET /wiki/rest/api/user/watch/space/{spaceKey}` — Get space watch status
- [[confluence_v1_add_space_watcher]] — `POST /wiki/rest/api/user/watch/space/{spaceKey}` — Add space watcher ✏️
- [[confluence_v1_remove_space_watch]] — `DELETE /wiki/rest/api/user/watch/space/{spaceKey}` — Remove space watch ✏️

## Dynamic modules

- [[Confluence v1 - Get modules]] — `GET /wiki/rest/atlassian-connect/1/app/module/dynamic` — Get modules 🔒
- [[Confluence v1 - Register modules]] — `POST /wiki/rest/atlassian-connect/1/app/module/dynamic` — Register modules ✏️🔒
- [[Confluence v1 - Remove modules]] — `DELETE /wiki/rest/atlassian-connect/1/app/module/dynamic` — Remove modules ✏️🔒

## Experimental

- [[confluence_v1_delete_page_tree]] — `DELETE /wiki/rest/api/content/{id}/pageTree` — Delete page tree ✏️
- [[confluence_v1_get_space_labels]] — `GET /wiki/rest/api/space/{spaceKey}/label` — Get Space Labels
- [[confluence_v1_add_labels_to_a_space]] — `POST /wiki/rest/api/space/{spaceKey}/label` — Add labels to a space ✏️
- [[confluence_v1_remove_label_from_a_space]] — `DELETE /wiki/rest/api/space/{spaceKey}/label` — Remove label from a space ✏️

## Group

- [[confluence_v1_get_groups]] — `GET /wiki/rest/api/group` — Get groups
- [[confluence_v1_create_new_user_group]] — `POST /wiki/rest/api/group` — Create new user group ✏️
- [[confluence_v1_get_group]] — `GET /wiki/rest/api/group/by-id` — Get group
- [[confluence_v1_delete_user_group]] — `DELETE /wiki/rest/api/group/by-id` — Delete user group ✏️
- [[confluence_v1_search_groups_by_partial_query]] — `GET /wiki/rest/api/group/picker` — Search groups by partial query
- [[confluence_v1_get_group_members]] — `GET /wiki/rest/api/group/{groupId}/membersByGroupId` — Get group members
- [[confluence_v1_add_member_to_group_by_groupid]] — `POST /wiki/rest/api/group/userByGroupId` — Add member to group by groupId ✏️
- [[confluence_v1_remove_member_from_group_using_group_id]] — `DELETE /wiki/rest/api/group/userByGroupId` — Remove member from group using group id ✏️

## Label info

- [[confluence_v1_get_label_information]] — `GET /wiki/rest/api/label` — Get label information

## Long-running task

- [[confluence_v1_get_long_running_tasks]] — `GET /wiki/rest/api/longtask` — Get long-running tasks
- [[confluence_v1_get_long_running_task]] — `GET /wiki/rest/api/longtask/{id}` — Get long-running task

## Relation

- [[confluence_v1_find_target_entities_related_to_a_source_entity]] — `GET /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}` — Find target entities related to a source entity
- [[confluence_v1_find_relationship_from_source_to_target]] — `GET /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}` — Find relationship from source to target
- [[confluence_v1_create_relationship]] — `PUT /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}` — Create relationship ✏️
- [[confluence_v1_delete_relationship]] — `DELETE /wiki/rest/api/relation/{relationName}/from/{sourceType}/{sourceKey}/to/{targetType}/{targetKey}` — Delete relationship ✏️
- [[confluence_v1_find_source_entities_related_to_a_target_entity]] — `GET /wiki/rest/api/relation/{relationName}/to/{targetType}/{targetKey}/from/{sourceType}` — Find source entities related to a target entity

## Search

- [[confluence_v1_search_content]] — `GET /wiki/rest/api/search` — Search content
- [[confluence_v1_search_users]] — `GET /wiki/rest/api/search/user` — Search users

## Settings

- [[confluence_v1_get_look_and_feel_settings]] — `GET /wiki/rest/api/settings/lookandfeel` — Get look and feel settings
- [[confluence_v1_select_look_and_feel_settings]] — `PUT /wiki/rest/api/settings/lookandfeel` — Select look and feel settings ✏️
- [[confluence_v1_update_look_and_feel_settings]] — `POST /wiki/rest/api/settings/lookandfeel/custom` — Update look and feel settings ✏️
- [[confluence_v1_reset_look_and_feel_settings]] — `DELETE /wiki/rest/api/settings/lookandfeel/custom` — Reset look and feel settings ✏️
- [[confluence_v1_get_system_info]] — `GET /wiki/rest/api/settings/systemInfo` — Get system info

## Space

- [[confluence_v1_create_space]] — `POST /wiki/rest/api/space` — Create space ✏️
- [[confluence_v1_create_private_space]] — `POST /wiki/rest/api/space/_private` — Create private space ✏️
- [[confluence_v1_update_space]] — `PUT /wiki/rest/api/space/{spaceKey}` — Update space ✏️
- [[confluence_v1_delete_space]] — `DELETE /wiki/rest/api/space/{spaceKey}` — Delete space ✏️

## Space permissions

- [[confluence_v1_add_new_permission_to_space]] — `POST /wiki/rest/api/space/{spaceKey}/permission` — Add new permission to space ✏️
- [[confluence_v1_add_new_custom_content_permission_to_space]] — `POST /wiki/rest/api/space/{spaceKey}/permission/custom-content` — Add new custom content permission to space ✏️
- [[confluence_v1_remove_a_space_permission]] — `DELETE /wiki/rest/api/space/{spaceKey}/permission/{id}` — Remove a space permission ✏️

## Space settings

- [[confluence_v1_get_space_settings]] — `GET /wiki/rest/api/space/{spaceKey}/settings` — Get space settings
- [[confluence_v1_update_space_settings]] — `PUT /wiki/rest/api/space/{spaceKey}/settings` — Update space settings ✏️

## Template

- [[confluence_v1_update_content_template]] — `PUT /wiki/rest/api/template` — Update content template ✏️
- [[confluence_v1_create_content_template]] — `POST /wiki/rest/api/template` — Create content template ✏️
- [[confluence_v1_get_blueprint_templates]] — `GET /wiki/rest/api/template/blueprint` — Get blueprint templates
- [[confluence_v1_get_content_templates]] — `GET /wiki/rest/api/template/page` — Get content templates
- [[confluence_v1_get_content_template]] — `GET /wiki/rest/api/template/{contentTemplateId}` — Get content template
- [[confluence_v1_remove_template]] — `DELETE /wiki/rest/api/template/{contentTemplateId}` — Remove template ✏️

## Themes

- [[confluence_v1_get_themes]] — `GET /wiki/rest/api/settings/theme` — Get themes
- [[confluence_v1_get_global_theme]] — `GET /wiki/rest/api/settings/theme/selected` — Get global theme
- [[confluence_v1_get_theme]] — `GET /wiki/rest/api/settings/theme/{themeKey}` — Get theme
- [[confluence_v1_get_space_theme]] — `GET /wiki/rest/api/space/{spaceKey}/theme` — Get space theme
- [[confluence_v1_set_space_theme]] — `PUT /wiki/rest/api/space/{spaceKey}/theme` — Set space theme ✏️
- [[confluence_v1_reset_space_theme]] — `DELETE /wiki/rest/api/space/{spaceKey}/theme` — Reset space theme ✏️

## Users

- [[confluence_v1_get_user]] — `GET /wiki/rest/api/user` — Get user
- [[confluence_v1_get_anonymous_user]] — `GET /wiki/rest/api/user/anonymous` — Get anonymous user
- [[confluence_v1_get_current_user]] — `GET /wiki/rest/api/user/current` — Get current user
- [[confluence_v1_get_group_memberships_for_user]] — `GET /wiki/rest/api/user/memberof` — Get group memberships for user
- [[confluence_v1_get_multiple_users_using_ids]] — `GET /wiki/rest/api/user/bulk` — Get multiple users using ids
- [[Confluence v1 - Get user email address]] — `GET /wiki/rest/api/user/email` — Get user email address 🔒
- [[Confluence v1 - Get user email addresses in batch]] — `GET /wiki/rest/api/user/email/bulk` — Get user email addresses in batch 🔒

## User properties

- [[confluence_v1_get_user_properties]] — `GET /wiki/rest/api/user/{userId}/property` — Get user properties
- [[confluence_v1_get_user_property]] — `GET /wiki/rest/api/user/{userId}/property/{key}` — Get user property
- [[confluence_v1_update_user_property]] — `PUT /wiki/rest/api/user/{userId}/property/{key}` — Update user property ✏️
- [[confluence_v1_create_user_property_by_key]] — `POST /wiki/rest/api/user/{userId}/property/{key}` — Create user property by key ✏️
- [[confluence_v1_delete_user_property]] — `DELETE /wiki/rest/api/user/{userId}/property/{key}` — Delete user property ✏️
