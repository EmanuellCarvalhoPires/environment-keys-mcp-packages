---
tags:
  - moc
  - mcp
  - api/app/jira
up: "[[MCP Tools]]"
---
# MCP - Jira v3

- **Tools:** 552 (exposed: 13; the others via `run_vault_tool`)
- **Requests only:** 43
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/jira/platform/rest/v3/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Announcement banner

- [[jira_get_announcement_banner_configuration]] — `GET /rest/api/3/announcementBanner` — Get announcement banner configuration
- [[jira_update_announcement_banner_configuration]] — `PUT /rest/api/3/announcementBanner` — Update announcement banner configuration ✏️

## App data policies

- [[jira_get_data_policy_for_the_workspace]] — `GET /rest/api/3/data-policy` — Get data policy for the workspace
- [[jira_get_data_policy_for_projects]] — `GET /rest/api/3/data-policy/project` — Get data policy for projects

## App migration

- [[Jira v3 - Bulk update custom field value]] — `PUT /rest/atlassian-connect/1/migration/field` — Bulk update custom field value ✏️🔒
- [[Jira v3 - Bulk update entity properties]] — `PUT /rest/atlassian-connect/1/migration/properties/{entityType}` — Bulk update entity properties ✏️🔒
- [[Jira v3 - Get workflow transition rule configurations]] — `POST /rest/atlassian-connect/1/migration/workflow/rule/search` — Get workflow transition rule configurations 🔒

## App properties

- [[Jira v3 - Get app properties]] — `GET /rest/atlassian-connect/1/addons/{addonKey}/properties` — Get app properties 🔒
- [[Jira v3 - Get app property]] — `GET /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}` — Get app property 🔒
- [[Jira v3 - Set app property]] — `PUT /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}` — Set app property ✏️🔒
- [[Jira v3 - Delete app property]] — `DELETE /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}` — Delete app property ✏️🔒
- [[Jira v3 - Get app property keys (Forge)]] — `GET /rest/forge/1/app/properties` — Get app property keys (Forge) 🔒
- [[Jira v3 - Get app property (Forge)]] — `GET /rest/forge/1/app/properties/{propertyKey}` — Get app property (Forge) 🔒
- [[Jira v3 - Set app property (Forge)]] — `PUT /rest/forge/1/app/properties/{propertyKey}` — Set app property (Forge) ✏️🔒
- [[Jira v3 - Delete app property (Forge)]] — `DELETE /rest/forge/1/app/properties/{propertyKey}` — Delete app property (Forge) ✏️🔒

## Application roles

- [[jira_get_all_application_roles]] — `GET /rest/api/3/applicationrole` — Get all application roles
- [[jira_get_application_role]] — `GET /rest/api/3/applicationrole/{key}` — Get application role

## Audit records

- [[jira_get_audit_records]] — `GET /rest/api/3/auditing/record` — Get audit records

## Avatars

- [[jira_get_system_avatars_by_type]] — `GET /rest/api/3/avatar/{type}/system` — Get system avatars by type
- [[jira_get_avatars]] — `GET /rest/api/3/universal_avatar/type/{type}/owner/{entityId}` — Get avatars
- [[jira_load_avatar]] — `POST /rest/api/3/universal_avatar/type/{type}/owner/{entityId}` — Load avatar ✏️
- [[jira_delete_avatar]] — `DELETE /rest/api/3/universal_avatar/type/{type}/owner/{owningObjectId}/avatar/{id}` — Delete avatar ✏️
- [[jira_get_avatar_image_by_type]] — `GET /rest/api/3/universal_avatar/view/type/{type}` — Get avatar image by type
- [[jira_get_avatar_image_by_id]] — `GET /rest/api/3/universal_avatar/view/type/{type}/avatar/{id}` — Get avatar image by ID
- [[jira_get_avatar_image_by_owner]] — `GET /rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}` — Get avatar image by owner

## Classification levels

- [[jira_get_all_classification_levels]] — `GET /rest/api/3/classification-levels` — Get all classification levels

## Dashboards

- [[jira_get_all_dashboards]] — `GET /rest/api/3/dashboard` — Get all dashboards
- [[jira_create_dashboard]] — `POST /rest/api/3/dashboard` — Create dashboard ✏️
- [[jira_bulk_edit_dashboards]] — `PUT /rest/api/3/dashboard/bulk/edit` — Bulk edit dashboards ✏️
- [[jira_get_available_gadgets]] — `GET /rest/api/3/dashboard/gadgets` — Get available gadgets
- [[jira_search_for_dashboards]] — `GET /rest/api/3/dashboard/search` — Search for dashboards
- [[jira_get_gadgets]] — `GET /rest/api/3/dashboard/{dashboardId}/gadget` — Get gadgets
- [[jira_add_gadget_to_dashboard]] — `POST /rest/api/3/dashboard/{dashboardId}/gadget` — Add gadget to dashboard ✏️
- [[jira_update_gadget_on_dashboard]] — `PUT /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}` — Update gadget on dashboard ✏️
- [[jira_remove_gadget_from_dashboard]] — `DELETE /rest/api/3/dashboard/{dashboardId}/gadget/{gadgetId}` — Remove gadget from dashboard ✏️
- [[jira_get_dashboard_item_property_keys]] — `GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties` — Get dashboard item property keys
- [[jira_get_dashboard_item_property]] — `GET /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}` — Get dashboard item property
- [[jira_set_dashboard_item_property]] — `PUT /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}` — Set dashboard item property ✏️
- [[jira_delete_dashboard_item_property]] — `DELETE /rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}` — Delete dashboard item property ✏️
- [[jira_get_dashboard]] — `GET /rest/api/3/dashboard/{id}` — Get dashboard
- [[jira_update_dashboard]] — `PUT /rest/api/3/dashboard/{id}` — Update dashboard ✏️
- [[jira_delete_dashboard]] — `DELETE /rest/api/3/dashboard/{id}` — Delete dashboard ✏️
- [[jira_copy_dashboard]] — `POST /rest/api/3/dashboard/{id}/copy` — Copy dashboard ✏️

## Dynamic modules

- [[Jira v3 - Get modules]] — `GET /rest/atlassian-connect/1/app/module/dynamic` — Get modules 🔒
- [[Jira v3 - Register modules]] — `POST /rest/atlassian-connect/1/app/module/dynamic` — Register modules ✏️🔒
- [[Jira v3 - Remove modules]] — `DELETE /rest/atlassian-connect/1/app/module/dynamic` — Remove modules ✏️🔒

## Field schemes

- [[jira_get_field_schemes]] — `GET /rest/api/3/config/fieldschemes` — Get field schemes
- [[jira_create_field_scheme]] — `POST /rest/api/3/config/fieldschemes` — Create field scheme ✏️
- [[jira_update_fields_associated_with_field_schemes]] — `PUT /rest/api/3/config/fieldschemes/fields` — Update fields associated with field schemes ✏️
- [[jira_remove_fields_associated_with_field_schemes]] — `DELETE /rest/api/3/config/fieldschemes/fields` — Remove fields associated with field schemes ✏️
- [[jira_update_field_parameters]] — `PUT /rest/api/3/config/fieldschemes/fields/parameters` — Update field parameters ✏️
- [[jira_remove_field_parameters]] — `DELETE /rest/api/3/config/fieldschemes/fields/parameters` — Remove field parameters ✏️
- [[jira_get_projects_with_field_schemes]] — `GET /rest/api/3/config/fieldschemes/projects` — Get projects with field schemes
- [[jira_associate_projects_to_field_schemes]] — `PUT /rest/api/3/config/fieldschemes/projects` — Associate projects to field schemes ✏️
- [[jira_get_field_scheme]] — `GET /rest/api/3/config/fieldschemes/{id}` — Get field scheme
- [[jira_update_field_scheme]] — `PUT /rest/api/3/config/fieldschemes/{id}` — Update field scheme ✏️
- [[jira_delete_a_field_scheme]] — `DELETE /rest/api/3/config/fieldschemes/{id}` — Delete a field scheme ✏️
- [[jira_clone_field_scheme]] — `POST /rest/api/3/config/fieldschemes/{id}/clone` — Clone field scheme ✏️
- [[jira_search_field_scheme_fields]] — `GET /rest/api/3/config/fieldschemes/{id}/fields` — Search field scheme fields
- [[jira_get_field_parameters]] — `GET /rest/api/3/config/fieldschemes/{id}/fields/{fieldId}/parameters` — Get field parameters
- [[jira_search_field_scheme_projects]] — `GET /rest/api/3/config/fieldschemes/{id}/projects` — Search field scheme projects

## Filter sharing

- [[jira_get_default_share_scope]] — `GET /rest/api/3/filter/defaultShareScope` — Get default share scope
- [[jira_set_default_share_scope]] — `PUT /rest/api/3/filter/defaultShareScope` — Set default share scope ✏️
- [[jira_get_share_permissions]] — `GET /rest/api/3/filter/{id}/permission` — Get share permissions
- [[jira_add_share_permission]] — `POST /rest/api/3/filter/{id}/permission` — Add share permission ✏️
- [[jira_get_share_permission]] — `GET /rest/api/3/filter/{id}/permission/{permissionId}` — Get share permission
- [[jira_delete_share_permission]] — `DELETE /rest/api/3/filter/{id}/permission/{permissionId}` — Delete share permission ✏️

## Filters

- [[jira_create_filter]] — `POST /rest/api/3/filter` — Create filter ✏️
- [[jira_get_favorite_filters]] — `GET /rest/api/3/filter/favourite` — Get favorite filters
- [[jira_get_my_filters]] — `GET /rest/api/3/filter/my` — Get my filters
- [[jira_search_for_filters]] — `GET /rest/api/3/filter/search` — Search for filters
- [[jira_get_filter]] — `GET /rest/api/3/filter/{id}` — Get filter
- [[jira_update_filter]] — `PUT /rest/api/3/filter/{id}` — Update filter ✏️
- [[jira_delete_filter]] — `DELETE /rest/api/3/filter/{id}` — Delete filter ✏️
- [[jira_get_columns]] — `GET /rest/api/3/filter/{id}/columns` — Get columns
- [[jira_set_columns]] — `PUT /rest/api/3/filter/{id}/columns` — Set columns ✏️
- [[jira_reset_columns]] — `DELETE /rest/api/3/filter/{id}/columns` — Reset columns ✏️
- [[jira_add_filter_as_favorite]] — `PUT /rest/api/3/filter/{id}/favourite` — Add filter as favorite ✏️
- [[jira_remove_filter_as_favorite]] — `DELETE /rest/api/3/filter/{id}/favourite` — Remove filter as favorite ✏️
- [[jira_change_filter_owner]] — `PUT /rest/api/3/filter/{id}/owner` — Change filter owner ✏️

## Group and user picker

- [[jira_find_users_and_groups]] — `GET /rest/api/3/groupuserpicker` — Find users and groups

## Groups

- [[jira_create_group]] — `POST /rest/api/3/group` — Create group ✏️
- [[jira_remove_group]] — `DELETE /rest/api/3/group` — Remove group ✏️
- [[jira_bulk_get_groups]] — `GET /rest/api/3/group/bulk` — Bulk get groups
- [[jira_get_users_from_group]] — `GET /rest/api/3/group/member` — Get users from group
- [[jira_add_user_to_group]] — `POST /rest/api/3/group/user` — Add user to group ✏️
- [[jira_remove_user_from_group]] — `DELETE /rest/api/3/group/user` — Remove user from group ✏️
- [[jira_find_groups]] — `GET /rest/api/3/groups/picker` — Find groups

## Issue attachments

- [[jira_get_attachment_content]] — `GET /rest/api/3/attachment/content/{id}` — Get attachment content
- [[jira_get_jira_attachment_settings]] — `GET /rest/api/3/attachment/meta` — Get Jira attachment settings
- [[jira_get_attachment_thumbnail]] — `GET /rest/api/3/attachment/thumbnail/{id}` — Get attachment thumbnail
- [[jira_get_attachment_metadata]] — `GET /rest/api/3/attachment/{id}` — Get attachment metadata
- [[jira_delete_attachment]] — `DELETE /rest/api/3/attachment/{id}` — Delete attachment ✏️
- [[jira_get_all_metadata_for_an_expanded_attachment]] — `GET /rest/api/3/attachment/{id}/expand/human` — Get all metadata for an expanded attachment
- [[jira_get_contents_metadata_for_an_expanded_attachment]] — `GET /rest/api/3/attachment/{id}/expand/raw` — Get contents metadata for an expanded attachment
- [[Jira v3 - Add attachment]] — `POST /rest/api/3/issue/{issueIdOrKey}/attachments` — Add attachment ✏️📎

## Issue bulk operations

- [[jira_bulk_delete_issues]] — `POST /rest/api/3/bulk/issues/delete` — Bulk delete issues ✏️
- [[jira_get_bulk_editable_fields]] — `GET /rest/api/3/bulk/issues/fields` — Get bulk editable fields
- [[jira_bulk_edit_issues]] — `POST /rest/api/3/bulk/issues/fields` — Bulk edit issues ✏️
- [[jira_bulk_move_issues]] — `POST /rest/api/3/bulk/issues/move` — Bulk move issues ✏️
- [[jira_get_available_transitions]] — `GET /rest/api/3/bulk/issues/transition` — Get available transitions
- [[jira_bulk_transition_issue_statuses]] — `POST /rest/api/3/bulk/issues/transition` — Bulk transition issue statuses ✏️
- [[jira_bulk_unwatch_issues]] — `POST /rest/api/3/bulk/issues/unwatch` — Bulk unwatch issues ✏️
- [[jira_bulk_watch_issues]] — `POST /rest/api/3/bulk/issues/watch` — Bulk watch issues ✏️
- [[jira_get_bulk_issue_operation_progress]] — `GET /rest/api/3/bulk/queue/{taskId}` — Get bulk issue operation progress

## Issue comment properties

- [[jira_get_comment_property_keys]] — `GET /rest/api/3/comment/{commentId}/properties` — Get comment property keys
- [[jira_get_comment_property]] — `GET /rest/api/3/comment/{commentId}/properties/{propertyKey}` — Get comment property
- [[jira_set_comment_property]] — `PUT /rest/api/3/comment/{commentId}/properties/{propertyKey}` — Set comment property ✏️
- [[jira_delete_comment_property]] — `DELETE /rest/api/3/comment/{commentId}/properties/{propertyKey}` — Delete comment property ✏️

## Issue comments

- [[jira_get_comments_by_ids]] — `POST /rest/api/3/comment/list` — Get comments by IDs
- [[jira_get_comments]] — `GET /rest/api/3/issue/{issueIdOrKey}/comment` — Get comments ⭐
- [[jira_add_comment]] — `POST /rest/api/3/issue/{issueIdOrKey}/comment` — Add comment ✏️⭐
- [[jira_get_comment]] — `GET /rest/api/3/issue/{issueIdOrKey}/comment/{id}` — Get comment
- [[jira_update_comment]] — `PUT /rest/api/3/issue/{issueIdOrKey}/comment/{id}` — Update comment ✏️
- [[jira_delete_comment]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/comment/{id}` — Delete comment ✏️

## Issue custom field associations

- [[jira_create_associations]] — `PUT /rest/api/3/field/association` — Create associations ✏️
- [[jira_remove_associations]] — `DELETE /rest/api/3/field/association` — Remove associations ✏️

## Issue custom field configuration (apps)

- [[Jira v3 - Bulk get custom field configurations]] — `POST /rest/api/3/app/field/context/configuration/list` — Bulk get custom field configurations 🔒
- [[Jira v3 - Get custom field configurations]] — `GET /rest/api/3/app/field/{fieldIdOrKey}/context/configuration` — Get custom field configurations 🔒
- [[Jira v3 - Update custom field configurations]] — `PUT /rest/api/3/app/field/{fieldIdOrKey}/context/configuration` — Update custom field configurations ✏️🔒

## Issue custom field contexts

- [[jira_get_custom_field_contexts]] — `GET /rest/api/3/field/{fieldId}/context` — Get custom field contexts
- [[jira_create_custom_field_context]] — `POST /rest/api/3/field/{fieldId}/context` — Create custom field context ✏️
- [[jira_get_custom_field_contexts_default_values]] — `GET /rest/api/3/field/{fieldId}/context/defaultValue` — Get custom field contexts default values
- [[jira_set_custom_field_contexts_default_values]] — `PUT /rest/api/3/field/{fieldId}/context/defaultValue` — Set custom field contexts default values ✏️
- [[jira_get_default_values_for_a_custom_field_grouped_by_context_an]] — `GET /rest/api/3/field/{fieldId}/context/defaultValues` — Get default values for a custom field grouped by context and issue type
- [[jira_get_issue_types_for_custom_field_context]] — `GET /rest/api/3/field/{fieldId}/context/issuetypemapping` — Get issue types for custom field context
- [[jira_get_custom_field_contexts_for_projects_and_issue_types]] — `POST /rest/api/3/field/{fieldId}/context/mapping` — Get custom field contexts for projects and issue types
- [[jira_get_project_mappings_for_custom_field_context]] — `GET /rest/api/3/field/{fieldId}/context/projectmapping` — Get project mappings for custom field context
- [[jira_update_custom_field_context]] — `PUT /rest/api/3/field/{fieldId}/context/{contextId}` — Update custom field context ✏️
- [[jira_delete_custom_field_context]] — `DELETE /rest/api/3/field/{fieldId}/context/{contextId}` — Delete custom field context ✏️
- [[jira_add_issue_types_to_context]] — `PUT /rest/api/3/field/{fieldId}/context/{contextId}/issuetype` — Add issue types to context ✏️
- [[jira_remove_issue_types_from_context]] — `POST /rest/api/3/field/{fieldId}/context/{contextId}/issuetype/remove` — Remove issue types from context ✏️
- [[jira_assign_custom_field_context_to_projects]] — `PUT /rest/api/3/field/{fieldId}/context/{contextId}/project` — Assign custom field context to projects ✏️
- [[jira_remove_custom_field_context_from_projects]] — `POST /rest/api/3/field/{fieldId}/context/{contextId}/project/remove` — Remove custom field context from projects ✏️

## Issue custom field options

- [[jira_get_custom_field_option]] — `GET /rest/api/3/customFieldOption/{id}` — Get custom field option
- [[jira_get_custom_field_options_context]] — `GET /rest/api/3/field/{fieldId}/context/{contextId}/option` — Get custom field options (context)
- [[jira_update_custom_field_options_context]] — `PUT /rest/api/3/field/{fieldId}/context/{contextId}/option` — Update custom field options (context) ✏️
- [[jira_create_custom_field_options_context]] — `POST /rest/api/3/field/{fieldId}/context/{contextId}/option` — Create custom field options (context) ✏️
- [[jira_reorder_custom_field_options_context]] — `PUT /rest/api/3/field/{fieldId}/context/{contextId}/option/move` — Reorder custom field options (context) ✏️
- [[jira_delete_custom_field_options_context]] — `DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}` — Delete custom field options (context) ✏️
- [[jira_replace_custom_field_options]] — `DELETE /rest/api/3/field/{fieldId}/context/{contextId}/option/{optionId}/issue` — Replace custom field options ✏️

## Issue custom field options (apps)

- [[Jira v3 - Get all issue field options]] — `GET /rest/api/3/field/{fieldKey}/option` — Get all issue field options 🔒
- [[Jira v3 - Create issue field option]] — `POST /rest/api/3/field/{fieldKey}/option` — Create issue field option ✏️🔒
- [[Jira v3 - Get selectable issue field options]] — `GET /rest/api/3/field/{fieldKey}/option/suggestions/edit` — Get selectable issue field options 🔒
- [[Jira v3 - Get visible issue field options]] — `GET /rest/api/3/field/{fieldKey}/option/suggestions/search` — Get visible issue field options 🔒
- [[Jira v3 - Get issue field option]] — `GET /rest/api/3/field/{fieldKey}/option/{optionId}` — Get issue field option 🔒
- [[Jira v3 - Update issue field option]] — `PUT /rest/api/3/field/{fieldKey}/option/{optionId}` — Update issue field option ✏️🔒
- [[Jira v3 - Delete issue field option]] — `DELETE /rest/api/3/field/{fieldKey}/option/{optionId}` — Delete issue field option ✏️🔒
- [[Jira v3 - Replace issue field option]] — `DELETE /rest/api/3/field/{fieldKey}/option/{optionId}/issue` — Replace issue field option ✏️🔒

## Issue custom field values (apps)

- [[Jira v3 - Update custom fields]] — `POST /rest/api/3/app/field/value` — Update custom fields ✏️🔒
- [[Jira v3 - Update custom field value]] — `PUT /rest/api/3/app/field/{fieldIdOrKey}/value` — Update custom field value ✏️🔒

## Issue fields

- [[jira_get_fields]] — `GET /rest/api/3/field` — Get fields
- [[jira_create_custom_field]] — `POST /rest/api/3/field` — Create custom field ✏️
- [[jira_get_fields_paginated]] — `GET /rest/api/3/field/search` — Get fields paginated
- [[jira_get_fields_in_trash_paginated]] — `GET /rest/api/3/field/search/trashed` — Get fields in trash paginated
- [[jira_update_custom_field]] — `PUT /rest/api/3/field/{fieldId}` — Update custom field ✏️
- [[jira_get_field_project_associations]] — `GET /rest/api/3/field/{fieldId}/association/project` — Get field project associations
- [[jira_get_contexts_for_a_field]] — `GET /rest/api/3/field/{fieldId}/contexts` — Get contexts for a field
- [[jira_delete_custom_field]] — `DELETE /rest/api/3/field/{id}` — Delete custom field ✏️
- [[jira_restore_custom_field_from_trash]] — `POST /rest/api/3/field/{id}/restore` — Restore custom field from trash ✏️
- [[jira_move_custom_field_to_trash]] — `POST /rest/api/3/field/{id}/trash` — Move custom field to trash ✏️
- [[jira_get_fields_for_projects]] — `GET /rest/api/3/projects/fields` — Get fields for projects

## Issue link types

- [[jira_get_issue_link_types]] — `GET /rest/api/3/issueLinkType` — Get issue link types
- [[jira_create_issue_link_type]] — `POST /rest/api/3/issueLinkType` — Create issue link type ✏️
- [[jira_get_issue_link_type]] — `GET /rest/api/3/issueLinkType/{issueLinkTypeId}` — Get issue link type
- [[jira_update_issue_link_type]] — `PUT /rest/api/3/issueLinkType/{issueLinkTypeId}` — Update issue link type ✏️
- [[jira_delete_issue_link_type]] — `DELETE /rest/api/3/issueLinkType/{issueLinkTypeId}` — Delete issue link type ✏️

## Issue links

- [[jira_create_issue_link]] — `POST /rest/api/3/issueLink` — Create issue link ✏️
- [[jira_get_issue_link]] — `GET /rest/api/3/issueLink/{linkId}` — Get issue link
- [[jira_delete_issue_link]] — `DELETE /rest/api/3/issueLink/{linkId}` — Delete issue link ✏️

## Issue navigator settings

- [[jira_get_issue_navigator_default_columns]] — `GET /rest/api/3/settings/columns` — Get issue navigator default columns
- [[Jira v3 - Set issue navigator default columns]] — `PUT /rest/api/3/settings/columns` — Set issue navigator default columns ✏️📎

## Issue notification schemes

- [[jira_get_notification_schemes_paginated]] — `GET /rest/api/3/notificationscheme` — Get notification schemes paginated
- [[jira_create_notification_scheme]] — `POST /rest/api/3/notificationscheme` — Create notification scheme ✏️
- [[jira_get_projects_using_notification_schemes_paginated]] — `GET /rest/api/3/notificationscheme/project` — Get projects using notification schemes paginated
- [[jira_get_notification_scheme]] — `GET /rest/api/3/notificationscheme/{id}` — Get notification scheme
- [[jira_update_notification_scheme]] — `PUT /rest/api/3/notificationscheme/{id}` — Update notification scheme ✏️
- [[jira_add_notifications_to_notification_scheme]] — `PUT /rest/api/3/notificationscheme/{id}/notification` — Add notifications to notification scheme ✏️
- [[jira_delete_notification_scheme]] — `DELETE /rest/api/3/notificationscheme/{notificationSchemeId}` — Delete notification scheme ✏️
- [[jira_remove_notification_from_notification_scheme]] — `DELETE /rest/api/3/notificationscheme/{notificationSchemeId}/notification/{notificationId}` — Remove notification from notification scheme ✏️

## Issue panels

- [[jira_bulk_pin_or_unpin_issue_panel_to_projects]] — `POST /rest/api/3/forge/panel/action/bulk/async` — Bulk pin or unpin issue panel to projects ✏️
- [[jira_get_issue_panel_pin_status_for_projects]] — `POST /rest/api/3/forge/panel/action/bulk/status` — Get issue panel pin status for projects

## Issue priorities

- [[jira_create_priority]] — `POST /rest/api/3/priority` — Create priority ✏️
- [[jira_set_default_priority]] — `PUT /rest/api/3/priority/default` — Set default priority ✏️
- [[jira_move_priorities]] — `PUT /rest/api/3/priority/move` — Move priorities ✏️
- [[jira_search_priorities]] — `GET /rest/api/3/priority/search` — Search priorities
- [[jira_get_priority]] — `GET /rest/api/3/priority/{id}` — Get priority
- [[jira_update_priority]] — `PUT /rest/api/3/priority/{id}` — Update priority ✏️
- [[jira_delete_priority]] — `DELETE /rest/api/3/priority/{id}` — Delete priority ✏️

## Issue properties

- [[jira_bulk_set_issues_properties_by_list]] — `POST /rest/api/3/issue/properties` — Bulk set issues properties by list ✏️
- [[jira_bulk_set_issue_properties_by_issue]] — `POST /rest/api/3/issue/properties/multi` — Bulk set issue properties by issue ✏️
- [[jira_bulk_set_issue_property]] — `PUT /rest/api/3/issue/properties/{propertyKey}` — Bulk set issue property ✏️
- [[jira_bulk_delete_issue_property]] — `DELETE /rest/api/3/issue/properties/{propertyKey}` — Bulk delete issue property ✏️
- [[jira_get_issue_property_keys]] — `GET /rest/api/3/issue/{issueIdOrKey}/properties` — Get issue property keys
- [[jira_get_issue_property]] — `GET /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}` — Get issue property
- [[jira_set_issue_property]] — `PUT /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}` — Set issue property ✏️
- [[jira_delete_issue_property]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}` — Delete issue property ✏️

## Issue redaction

- [[jira_redact]] — `POST /rest/api/3/redact` — Redact ✏️
- [[jira_get_redaction_status]] — `GET /rest/api/3/redact/status/{jobId}` — Get redaction status

## Issue remote links

- [[jira_get_remote_issue_links]] — `GET /rest/api/3/issue/{issueIdOrKey}/remotelink` — Get remote issue links
- [[jira_create_or_update_remote_issue_link]] — `POST /rest/api/3/issue/{issueIdOrKey}/remotelink` — Create or update remote issue link ✏️
- [[jira_delete_remote_issue_link_by_global_id]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink` — Delete remote issue link by global ID ✏️
- [[jira_get_remote_issue_link_by_id]] — `GET /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}` — Get remote issue link by ID
- [[jira_update_remote_issue_link_by_id]] — `PUT /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}` — Update remote issue link by ID ✏️
- [[jira_delete_remote_issue_link_by_id]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}` — Delete remote issue link by ID ✏️

## Issue resolutions

- [[jira_get_resolutions]] — `GET /rest/api/3/resolution` — Get resolutions
- [[jira_create_resolution]] — `POST /rest/api/3/resolution` — Create resolution ✏️
- [[jira_set_default_resolution]] — `PUT /rest/api/3/resolution/default` — Set default resolution ✏️
- [[jira_move_resolutions]] — `PUT /rest/api/3/resolution/move` — Move resolutions ✏️
- [[jira_search_resolutions]] — `GET /rest/api/3/resolution/search` — Search resolutions
- [[jira_get_resolution]] — `GET /rest/api/3/resolution/{id}` — Get resolution
- [[jira_update_resolution]] — `PUT /rest/api/3/resolution/{id}` — Update resolution ✏️
- [[jira_delete_resolution]] — `DELETE /rest/api/3/resolution/{id}` — Delete resolution ✏️

## Issue search

- [[jira_get_issue_picker_suggestions]] — `GET /rest/api/3/issue/picker` — Get issue picker suggestions
- [[jira_check_issues_against_jql]] — `POST /rest/api/3/jql/match` — Check issues against JQL
- [[jira_count_issues_using_jql]] — `POST /rest/api/3/search/approximate-count` — Count issues using JQL
- [[jira_search_for_issues_using_jql_enhanced_search_get]] — `GET /rest/api/3/search/jql` — Search for issues using JQL enhanced search (GET) ⭐
- [[jira_search_for_issues_using_jql_enhanced_search_post]] — `POST /rest/api/3/search/jql` — Search for issues using JQL enhanced search (POST)

## Issue security level

- [[jira_get_issue_security_level_members_by_issue_security_scheme]] — `GET /rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members` — Get issue security level members by issue security scheme
- [[jira_get_issue_security_level]] — `GET /rest/api/3/securitylevel/{id}` — Get issue security level

## Issue security schemes

- [[jira_get_issue_security_schemes]] — `GET /rest/api/3/issuesecurityschemes` — Get issue security schemes
- [[jira_create_issue_security_scheme]] — `POST /rest/api/3/issuesecurityschemes` — Create issue security scheme ✏️
- [[jira_get_issue_security_levels]] — `GET /rest/api/3/issuesecurityschemes/level` — Get issue security levels
- [[jira_set_default_issue_security_levels]] — `PUT /rest/api/3/issuesecurityschemes/level/default` — Set default issue security levels ✏️
- [[jira_get_issue_security_level_members]] — `GET /rest/api/3/issuesecurityschemes/level/member` — Get issue security level members
- [[jira_get_projects_using_issue_security_schemes]] — `GET /rest/api/3/issuesecurityschemes/project` — Get projects using issue security schemes
- [[jira_associate_security_scheme_to_project]] — `PUT /rest/api/3/issuesecurityschemes/project` — Associate security scheme to project ✏️
- [[jira_search_issue_security_schemes]] — `GET /rest/api/3/issuesecurityschemes/search` — Search issue security schemes
- [[jira_get_issue_security_scheme]] — `GET /rest/api/3/issuesecurityschemes/{id}` — Get issue security scheme
- [[jira_update_issue_security_scheme]] — `PUT /rest/api/3/issuesecurityschemes/{id}` — Update issue security scheme ✏️
- [[jira_delete_issue_security_scheme]] — `DELETE /rest/api/3/issuesecurityschemes/{schemeId}` — Delete issue security scheme ✏️
- [[jira_add_issue_security_levels]] — `PUT /rest/api/3/issuesecurityschemes/{schemeId}/level` — Add issue security levels ✏️
- [[jira_update_issue_security_level]] — `PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}` — Update issue security level ✏️
- [[jira_remove_issue_security_level]] — `DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}` — Remove issue security level ✏️
- [[jira_add_issue_security_level_members]] — `PUT /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member` — Add issue security level members ✏️
- [[jira_remove_member_from_issue_security_level]] — `DELETE /rest/api/3/issuesecurityschemes/{schemeId}/level/{levelId}/member/{memberId}` — Remove member from issue security level ✏️

## Issue type properties

- [[jira_get_issue_type_property_keys]] — `GET /rest/api/3/issuetype/{issueTypeId}/properties` — Get issue type property keys
- [[jira_get_issue_type_property]] — `GET /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}` — Get issue type property
- [[jira_set_issue_type_property]] — `PUT /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}` — Set issue type property ✏️
- [[jira_delete_issue_type_property]] — `DELETE /rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}` — Delete issue type property ✏️

## Issue type schemes

- [[jira_get_all_issue_type_schemes]] — `GET /rest/api/3/issuetypescheme` — Get all issue type schemes
- [[jira_create_issue_type_scheme]] — `POST /rest/api/3/issuetypescheme` — Create issue type scheme ✏️
- [[jira_get_issue_type_scheme_items]] — `GET /rest/api/3/issuetypescheme/mapping` — Get issue type scheme items
- [[jira_get_issue_type_schemes_for_projects]] — `GET /rest/api/3/issuetypescheme/project` — Get issue type schemes for projects
- [[jira_assign_issue_type_scheme_to_project]] — `PUT /rest/api/3/issuetypescheme/project` — Assign issue type scheme to project ✏️
- [[jira_update_issue_type_scheme]] — `PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}` — Update issue type scheme ✏️
- [[jira_delete_issue_type_scheme]] — `DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}` — Delete issue type scheme ✏️
- [[jira_add_issue_types_to_issue_type_scheme]] — `PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype` — Add issue types to issue type scheme ✏️
- [[jira_change_order_of_issue_types]] — `PUT /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/move` — Change order of issue types ✏️
- [[jira_remove_issue_type_from_issue_type_scheme]] — `DELETE /rest/api/3/issuetypescheme/{issueTypeSchemeId}/issuetype/{issueTypeId}` — Remove issue type from issue type scheme ✏️

## Issue type screen schemes

- [[jira_get_issue_type_screen_schemes]] — `GET /rest/api/3/issuetypescreenscheme` — Get issue type screen schemes
- [[jira_create_issue_type_screen_scheme]] — `POST /rest/api/3/issuetypescreenscheme` — Create issue type screen scheme ✏️
- [[jira_get_issue_type_screen_scheme_items]] — `GET /rest/api/3/issuetypescreenscheme/mapping` — Get issue type screen scheme items
- [[jira_get_issue_type_screen_schemes_for_projects]] — `GET /rest/api/3/issuetypescreenscheme/project` — Get issue type screen schemes for projects
- [[jira_assign_issue_type_screen_scheme_to_project]] — `PUT /rest/api/3/issuetypescreenscheme/project` — Assign issue type screen scheme to project ✏️
- [[jira_update_issue_type_screen_scheme]] — `PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}` — Update issue type screen scheme ✏️
- [[jira_delete_issue_type_screen_scheme]] — `DELETE /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}` — Delete issue type screen scheme ✏️
- [[jira_append_mappings_to_issue_type_screen_scheme]] — `PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping` — Append mappings to issue type screen scheme ✏️
- [[jira_update_issue_type_screen_scheme_default_screen_scheme]] — `PUT /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/default` — Update issue type screen scheme default screen scheme ✏️
- [[jira_remove_mappings_from_issue_type_screen_scheme]] — `POST /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/mapping/remove` — Remove mappings from issue type screen scheme ✏️
- [[jira_get_issue_type_screen_scheme_projects]] — `GET /rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project` — Get issue type screen scheme projects

## Issue types

- [[jira_get_all_issue_types_for_user]] — `GET /rest/api/3/issuetype` — Get all issue types for user
- [[jira_create_issue_type]] — `POST /rest/api/3/issuetype` — Create issue type ✏️
- [[jira_get_issue_types_for_project]] — `GET /rest/api/3/issuetype/project` — Get issue types for project
- [[jira_get_issue_type]] — `GET /rest/api/3/issuetype/{id}` — Get issue type
- [[jira_update_issue_type]] — `PUT /rest/api/3/issuetype/{id}` — Update issue type ✏️
- [[jira_delete_issue_type]] — `DELETE /rest/api/3/issuetype/{id}` — Delete issue type ✏️
- [[jira_get_alternative_issue_types]] — `GET /rest/api/3/issuetype/{id}/alternatives` — Get alternative issue types
- [[jira_load_issue_type_avatar]] — `POST /rest/api/3/issuetype/{id}/avatar2` — Load issue type avatar ✏️

## Issue votes

- [[jira_get_votes]] — `GET /rest/api/3/issue/{issueIdOrKey}/votes` — Get votes
- [[jira_add_vote]] — `POST /rest/api/3/issue/{issueIdOrKey}/votes` — Add vote ✏️
- [[jira_delete_vote]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/votes` — Delete vote ✏️

## Issue watchers

- [[jira_get_is_watching_issue_bulk]] — `POST /rest/api/3/issue/watching` — Get is watching issue bulk
- [[jira_get_issue_watchers]] — `GET /rest/api/3/issue/{issueIdOrKey}/watchers` — Get issue watchers
- [[jira_add_watcher]] — `POST /rest/api/3/issue/{issueIdOrKey}/watchers` — Add watcher ✏️
- [[jira_delete_watcher]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/watchers` — Delete watcher ✏️

## Issue worklog properties

- [[jira_get_worklog_property_keys]] — `GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties` — Get worklog property keys
- [[jira_get_worklog_property]] — `GET /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}` — Get worklog property
- [[jira_set_worklog_property]] — `PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}` — Set worklog property ✏️
- [[jira_delete_worklog_property]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}` — Delete worklog property ✏️

## Issue worklogs

- [[jira_get_issue_worklogs]] — `GET /rest/api/3/issue/{issueIdOrKey}/worklog` — Get issue worklogs
- [[jira_add_worklog]] — `POST /rest/api/3/issue/{issueIdOrKey}/worklog` — Add worklog ✏️
- [[jira_bulk_delete_worklogs]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog` — Bulk delete worklogs ✏️
- [[jira_bulk_move_worklogs]] — `POST /rest/api/3/issue/{issueIdOrKey}/worklog/move` — Bulk move worklogs ✏️
- [[jira_get_worklog]] — `GET /rest/api/3/issue/{issueIdOrKey}/worklog/{id}` — Get worklog
- [[jira_update_worklog]] — `PUT /rest/api/3/issue/{issueIdOrKey}/worklog/{id}` — Update worklog ✏️
- [[jira_delete_worklog]] — `DELETE /rest/api/3/issue/{issueIdOrKey}/worklog/{id}` — Delete worklog ✏️
- [[jira_get_ids_of_deleted_worklogs]] — `GET /rest/api/3/worklog/deleted` — Get IDs of deleted worklogs
- [[jira_get_worklogs]] — `POST /rest/api/3/worklog/list` — Get worklogs
- [[jira_get_ids_of_updated_worklogs]] — `GET /rest/api/3/worklog/updated` — Get IDs of updated worklogs

## Issues

- [[jira_bulk_fetch_changelogs]] — `POST /rest/api/3/changelog/bulkfetch` — Bulk fetch changelogs
- [[jira_get_events]] — `GET /rest/api/3/events` — Get events
- [[jira_create_issue]] — `POST /rest/api/3/issue` — Create issue ✏️⭐
- [[jira_archive_issue_s_by_issue_id_key]] — `PUT /rest/api/3/issue/archive` — Archive issue(s) by issue ID/key ✏️
- [[jira_archive_issue_s_by_jql]] — `POST /rest/api/3/issue/archive` — Archive issue(s) by JQL ✏️
- [[jira_bulk_create_issue]] — `POST /rest/api/3/issue/bulk` — Bulk create issue ✏️
- [[jira_bulk_fetch_issues]] — `POST /rest/api/3/issue/bulkfetch` — Bulk fetch issues
- [[jira_get_create_metadata_issue_types_for_a_project]] — `GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes` — Get create metadata issue types for a project
- [[jira_get_create_field_metadata_for_a_project_and_issue_type_id]] — `GET /rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}` — Get create field metadata for a project and issue type id
- [[jira_get_issue_adf_limit_report]] — `GET /rest/api/3/issue/limit/adf/report` — Get issue adf limit report
- [[jira_get_issue_limit_report]] — `GET /rest/api/3/issue/limit/report` — Get issue limit report
- [[jira_unarchive_issue_s_by_issue_keys_id]] — `PUT /rest/api/3/issue/unarchive` — Unarchive issue(s) by issue keys/ID ✏️
- [[jira_get_issue]] — `GET /rest/api/3/issue/{issueIdOrKey}` — Get issue ⭐
- [[jira_edit_issue]] — `PUT /rest/api/3/issue/{issueIdOrKey}` — Edit issue ✏️⭐
- [[jira_delete_issue]] — `DELETE /rest/api/3/issue/{issueIdOrKey}` — Delete issue ✏️
- [[jira_assign_issue]] — `PUT /rest/api/3/issue/{issueIdOrKey}/assignee` — Assign issue ✏️⭐
- [[jira_get_changelogs]] — `GET /rest/api/3/issue/{issueIdOrKey}/changelog` — Get changelogs
- [[jira_get_changelogs_by_ids]] — `POST /rest/api/3/issue/{issueIdOrKey}/changelog/list` — Get changelogs by IDs
- [[jira_get_edit_issue_metadata]] — `GET /rest/api/3/issue/{issueIdOrKey}/editmeta` — Get edit issue metadata
- [[jira_send_notification_for_issue]] — `POST /rest/api/3/issue/{issueIdOrKey}/notify` — Send notification for issue ✏️
- [[jira_get_transitions]] — `GET /rest/api/3/issue/{issueIdOrKey}/transitions` — Get transitions ⭐
- [[jira_transition_issue]] — `POST /rest/api/3/issue/{issueIdOrKey}/transitions` — Transition issue ✏️⭐
- [[jira_export_archived_issue_s]] — `PUT /rest/api/3/issues/archive/export` — Export archived issue(s) ✏️

## JQL

- [[jira_get_field_reference_data_get]] — `GET /rest/api/3/jql/autocompletedata` — Get field reference data (GET)
- [[jira_get_field_reference_data_post]] — `POST /rest/api/3/jql/autocompletedata` — Get field reference data (POST)
- [[jira_get_field_auto_complete_suggestions]] — `GET /rest/api/3/jql/autocompletedata/suggestions` — Get field auto complete suggestions
- [[jira_parse_jql_query]] — `POST /rest/api/3/jql/parse` — Parse JQL query
- [[jira_convert_user_identifiers_to_account_ids_in_jql_queries]] — `POST /rest/api/3/jql/pdcleaner` — Convert user identifiers to account IDs in JQL queries
- [[jira_sanitize_jql_queries]] — `POST /rest/api/3/jql/sanitize` — Sanitize JQL queries

## JQL functions (apps)

- [[Jira v3 - Get precomputations (apps)]] — `GET /rest/api/3/jql/function/computation` — Get precomputations (apps) 🔒
- [[Jira v3 - Update precomputations (apps)]] — `POST /rest/api/3/jql/function/computation` — Update precomputations (apps) ✏️🔒
- [[Jira v3 - Get precomputations by ID (apps)]] — `POST /rest/api/3/jql/function/computation/search` — Get precomputations by ID (apps) 🔒

## Jira expressions

- [[jira_analyse_jira_expression]] — `POST /rest/api/3/expression/analyse` — Analyse Jira expression
- [[jira_evaluate_jira_expression_using_enhanced_search_api]] — `POST /rest/api/3/expression/evaluate` — Evaluate Jira expression using enhanced search API

## Jira settings

- [[jira_get_application_property]] — `GET /rest/api/3/application-properties` — Get application property
- [[jira_get_advanced_settings]] — `GET /rest/api/3/application-properties/advanced-settings` — Get advanced settings
- [[jira_set_application_property]] — `PUT /rest/api/3/application-properties/{id}` — Set application property ✏️
- [[jira_get_global_settings]] — `GET /rest/api/3/configuration` — Get global settings

## Labels

- [[jira_get_all_labels]] — `GET /rest/api/3/label` — Get all labels

## License metrics

- [[jira_get_license]] — `GET /rest/api/3/instance/license` — Get license
- [[jira_get_approximate_license_count]] — `GET /rest/api/3/license/approximateLicenseCount` — Get approximate license count
- [[jira_get_approximate_application_license_count]] — `GET /rest/api/3/license/approximateLicenseCount/product/{applicationKey}` — Get approximate application license count

## Migration of Connect modules to Forge

- [[Jira v3 - Get Connect issue field migration task]] — `GET /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task` — Get Connect issue field migration task 🔒
- [[Jira v3 - Submit Connect issue field migration task]] — `POST /rest/atlassian-connect/1/migration/{connectKey}/{jiraIssueFieldsKey}/task` — Submit Connect issue field migration task ✏️🔒

## Myself

- [[jira_get_preference]] — `GET /rest/api/3/mypreferences` — Get preference
- [[jira_set_preference]] — `PUT /rest/api/3/mypreferences` — Set preference ✏️
- [[jira_delete_preference]] — `DELETE /rest/api/3/mypreferences` — Delete preference ✏️
- [[jira_get_locale]] — `GET /rest/api/3/mypreferences/locale` — Get locale
- [[jira_get_current_user]] — `GET /rest/api/3/myself` — Get current user ⭐

## Permission schemes

- [[jira_get_all_permission_schemes]] — `GET /rest/api/3/permissionscheme` — Get all permission schemes
- [[jira_create_permission_scheme]] — `POST /rest/api/3/permissionscheme` — Create permission scheme ✏️
- [[jira_get_permission_scheme]] — `GET /rest/api/3/permissionscheme/{schemeId}` — Get permission scheme
- [[jira_update_permission_scheme]] — `PUT /rest/api/3/permissionscheme/{schemeId}` — Update permission scheme ✏️
- [[jira_delete_permission_scheme]] — `DELETE /rest/api/3/permissionscheme/{schemeId}` — Delete permission scheme ✏️
- [[jira_get_permission_scheme_grants]] — `GET /rest/api/3/permissionscheme/{schemeId}/permission` — Get permission scheme grants
- [[jira_create_permission_grant]] — `POST /rest/api/3/permissionscheme/{schemeId}/permission` — Create permission grant ✏️
- [[jira_get_permission_scheme_grant]] — `GET /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}` — Get permission scheme grant
- [[jira_delete_permission_scheme_grant]] — `DELETE /rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}` — Delete permission scheme grant ✏️

## Permissions

- [[jira_get_my_permissions]] — `GET /rest/api/3/mypermissions` — Get my permissions
- [[jira_get_all_permissions]] — `GET /rest/api/3/permissions` — Get all permissions
- [[jira_get_bulk_permissions]] — `POST /rest/api/3/permissions/check` — Get bulk permissions
- [[jira_get_permitted_projects]] — `POST /rest/api/3/permissions/project` — Get permitted projects

## Plans

- [[jira_get_plans_paginated]] — `GET /rest/api/3/plans/plan` — Get plans paginated
- [[jira_create_plan]] — `POST /rest/api/3/plans/plan` — Create plan ✏️
- [[jira_get_plan]] — `GET /rest/api/3/plans/plan/{planId}` — Get plan
- [[jira_update_plan]] — `PUT /rest/api/3/plans/plan/{planId}` — Update plan ✏️
- [[jira_archive_plan]] — `PUT /rest/api/3/plans/plan/{planId}/archive` — Archive plan ✏️
- [[jira_duplicate_plan]] — `POST /rest/api/3/plans/plan/{planId}/duplicate` — Duplicate plan ✏️
- [[jira_trash_plan]] — `PUT /rest/api/3/plans/plan/{planId}/trash` — Trash plan ✏️

## Priority schemes

- [[jira_get_priority_schemes]] — `GET /rest/api/3/priorityscheme` — Get priority schemes
- [[jira_create_priority_scheme]] — `POST /rest/api/3/priorityscheme` — Create priority scheme ✏️
- [[jira_suggested_priorities_for_mappings]] — `POST /rest/api/3/priorityscheme/mappings` — Suggested priorities for mappings ✏️
- [[jira_get_available_priorities_by_priority_scheme]] — `GET /rest/api/3/priorityscheme/priorities/available` — Get available priorities by priority scheme
- [[jira_update_priority_scheme]] — `PUT /rest/api/3/priorityscheme/{schemeId}` — Update priority scheme ✏️
- [[jira_delete_priority_scheme]] — `DELETE /rest/api/3/priorityscheme/{schemeId}` — Delete priority scheme ✏️
- [[jira_get_priorities_by_priority_scheme]] — `GET /rest/api/3/priorityscheme/{schemeId}/priorities` — Get priorities by priority scheme
- [[jira_get_projects_by_priority_scheme]] — `GET /rest/api/3/priorityscheme/{schemeId}/projects` — Get projects by priority scheme

## Project avatars

- [[jira_set_project_avatar]] — `PUT /rest/api/3/project/{projectIdOrKey}/avatar` — Set project avatar ✏️
- [[jira_delete_project_avatar]] — `DELETE /rest/api/3/project/{projectIdOrKey}/avatar/{id}` — Delete project avatar ✏️
- [[jira_load_project_avatar]] — `POST /rest/api/3/project/{projectIdOrKey}/avatar2` — Load project avatar ✏️
- [[jira_get_all_project_avatars]] — `GET /rest/api/3/project/{projectIdOrKey}/avatars` — Get all project avatars

## Project categories

- [[jira_get_all_project_categories]] — `GET /rest/api/3/projectCategory` — Get all project categories
- [[jira_create_project_category]] — `POST /rest/api/3/projectCategory` — Create project category ✏️
- [[jira_get_project_category_by_id]] — `GET /rest/api/3/projectCategory/{id}` — Get project category by ID
- [[jira_update_project_category]] — `PUT /rest/api/3/projectCategory/{id}` — Update project category ✏️
- [[jira_delete_project_category]] — `DELETE /rest/api/3/projectCategory/{id}` — Delete project category ✏️

## Project classification levels

- [[jira_get_the_classification_configuration_for_a_project]] — `GET /rest/api/3/project/{projectIdOrKey}/classification-config` — Get the classification configuration for a project
- [[jira_get_the_default_data_classification_level_of_a_project]] — `GET /rest/api/3/project/{projectIdOrKey}/classification-level/default` — Get the default data classification level of a project
- [[jira_update_the_default_data_classification_level_of_a_project]] — `PUT /rest/api/3/project/{projectIdOrKey}/classification-level/default` — Update the default data classification level of a project ✏️
- [[jira_remove_the_default_data_classification_level_from_a_project]] — `DELETE /rest/api/3/project/{projectIdOrKey}/classification-level/default` — Remove the default data classification level from a project ✏️

## Project components

- [[jira_find_components_for_projects]] — `GET /rest/api/3/component` — Find components for projects
- [[jira_create_component]] — `POST /rest/api/3/component` — Create component ✏️
- [[jira_get_component]] — `GET /rest/api/3/component/{id}` — Get component
- [[jira_update_component]] — `PUT /rest/api/3/component/{id}` — Update component ✏️
- [[jira_delete_component]] — `DELETE /rest/api/3/component/{id}` — Delete component ✏️
- [[jira_get_component_issues_count]] — `GET /rest/api/3/component/{id}/relatedIssueCounts` — Get component issues count
- [[jira_get_project_components_paginated]] — `GET /rest/api/3/project/{projectIdOrKey}/component` — Get project components paginated
- [[jira_get_project_components]] — `GET /rest/api/3/project/{projectIdOrKey}/components` — Get project components

## Project email

- [[jira_get_project_s_sender_email]] — `GET /rest/api/3/project/{projectId}/email` — Get project's sender email
- [[jira_set_project_s_sender_email]] — `PUT /rest/api/3/project/{projectId}/email` — Set project's sender email ✏️

## Project features

- [[jira_get_project_features]] — `GET /rest/api/3/project/{projectIdOrKey}/features` — Get project features
- [[jira_set_project_feature_state]] — `PUT /rest/api/3/project/{projectIdOrKey}/features/{featureKey}` — Set project feature state ✏️

## Project key and name validation

- [[jira_validate_project_key]] — `GET /rest/api/3/projectvalidate/key` — Validate project key
- [[jira_get_valid_project_key]] — `GET /rest/api/3/projectvalidate/validProjectKey` — Get valid project key
- [[jira_get_valid_project_name]] — `GET /rest/api/3/projectvalidate/validProjectName` — Get valid project name

## Project permission schemes

- [[jira_get_project_issue_security_scheme]] — `GET /rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme` — Get project issue security scheme
- [[jira_get_assigned_permission_scheme]] — `GET /rest/api/3/project/{projectKeyOrId}/permissionscheme` — Get assigned permission scheme
- [[jira_assign_permission_scheme]] — `PUT /rest/api/3/project/{projectKeyOrId}/permissionscheme` — Assign permission scheme ✏️
- [[jira_get_project_issue_security_levels]] — `GET /rest/api/3/project/{projectKeyOrId}/securitylevel` — Get project issue security levels

## Project properties

- [[jira_get_project_property_keys]] — `GET /rest/api/3/project/{projectIdOrKey}/properties` — Get project property keys
- [[jira_get_project_property]] — `GET /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}` — Get project property
- [[jira_set_project_property]] — `PUT /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}` — Set project property ✏️
- [[jira_delete_project_property]] — `DELETE /rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}` — Delete project property ✏️

## Project role actors

- [[jira_set_actors_for_project_role]] — `PUT /rest/api/3/project/{projectIdOrKey}/role/{id}` — Set actors for project role ✏️
- [[jira_add_actors_to_project_role]] — `POST /rest/api/3/project/{projectIdOrKey}/role/{id}` — Add actors to project role ✏️
- [[jira_delete_actors_from_project_role]] — `DELETE /rest/api/3/project/{projectIdOrKey}/role/{id}` — Delete actors from project role ✏️
- [[jira_get_default_actors_for_project_role]] — `GET /rest/api/3/role/{id}/actors` — Get default actors for project role
- [[jira_add_default_actors_to_project_role]] — `POST /rest/api/3/role/{id}/actors` — Add default actors to project role ✏️
- [[jira_delete_default_actors_from_project_role]] — `DELETE /rest/api/3/role/{id}/actors` — Delete default actors from project role ✏️

## Project roles

- [[jira_get_project_roles_for_project]] — `GET /rest/api/3/project/{projectIdOrKey}/role` — Get project roles for project
- [[jira_get_project_role_for_project]] — `GET /rest/api/3/project/{projectIdOrKey}/role/{id}` — Get project role for project
- [[jira_get_project_role_details]] — `GET /rest/api/3/project/{projectIdOrKey}/roledetails` — Get project role details
- [[jira_get_all_project_roles]] — `GET /rest/api/3/role` — Get all project roles
- [[jira_create_project_role]] — `POST /rest/api/3/role` — Create project role ✏️
- [[jira_get_project_role_by_id]] — `GET /rest/api/3/role/{id}` — Get project role by ID
- [[jira_fully_update_project_role]] — `PUT /rest/api/3/role/{id}` — Fully update project role ✏️
- [[jira_partial_update_project_role]] — `POST /rest/api/3/role/{id}` — Partial update project role ✏️
- [[jira_delete_project_role]] — `DELETE /rest/api/3/role/{id}` — Delete project role ✏️

## Project templates

- [[jira_create_custom_project]] — `POST /rest/api/3/project-template` — Create custom project ✏️
- [[jira_edit_a_custom_project_template]] — `PUT /rest/api/3/project-template/edit-template` — Edit a custom project template ✏️
- [[jira_gets_a_custom_project_template]] — `GET /rest/api/3/project-template/live-template` — Gets a custom project template
- [[jira_deletes_a_custom_project_template]] — `DELETE /rest/api/3/project-template/remove-template` — Deletes a custom project template ✏️
- [[jira_save_a_custom_project_template]] — `POST /rest/api/3/project-template/save-template` — Save a custom project template ✏️

## Project types

- [[jira_get_all_project_types]] — `GET /rest/api/3/project/type` — Get all project types
- [[jira_get_licensed_project_types]] — `GET /rest/api/3/project/type/accessible` — Get licensed project types
- [[jira_get_project_type_by_key]] — `GET /rest/api/3/project/type/{projectTypeKey}` — Get project type by key
- [[jira_get_accessible_project_type_by_key]] — `GET /rest/api/3/project/type/{projectTypeKey}/accessible` — Get accessible project type by key

## Project versions

- [[jira_get_project_versions_paginated]] — `GET /rest/api/3/project/{projectIdOrKey}/version` — Get project versions paginated
- [[jira_get_project_versions]] — `GET /rest/api/3/project/{projectIdOrKey}/versions` — Get project versions
- [[jira_create_version]] — `POST /rest/api/3/version` — Create version ✏️
- [[jira_get_version]] — `GET /rest/api/3/version/{id}` — Get version
- [[jira_update_version]] — `PUT /rest/api/3/version/{id}` — Update version ✏️
- [[jira_merge_versions]] — `PUT /rest/api/3/version/{id}/mergeto/{moveIssuesTo}` — Merge versions ✏️
- [[jira_move_version]] — `POST /rest/api/3/version/{id}/move` — Move version ✏️
- [[jira_get_version_s_related_issues_count]] — `GET /rest/api/3/version/{id}/relatedIssueCounts` — Get version's related issues count
- [[jira_get_related_work]] — `GET /rest/api/3/version/{id}/relatedwork` — Get related work
- [[jira_update_related_work]] — `PUT /rest/api/3/version/{id}/relatedwork` — Update related work ✏️
- [[jira_create_related_work]] — `POST /rest/api/3/version/{id}/relatedwork` — Create related work ✏️
- [[jira_delete_and_replace_version]] — `POST /rest/api/3/version/{id}/removeAndSwap` — Delete and replace version ✏️
- [[jira_get_version_s_unresolved_issues_count]] — `GET /rest/api/3/version/{id}/unresolvedIssueCount` — Get version's unresolved issues count
- [[jira_delete_related_work]] — `DELETE /rest/api/3/version/{versionId}/relatedwork/{relatedWorkId}` — Delete related work ✏️

## Projects

- [[jira_get_all_projects]] — `GET /rest/api/3/project` — Get all projects
- [[jira_create_project]] — `POST /rest/api/3/project` — Create project ✏️
- [[jira_get_recent_projects]] — `GET /rest/api/3/project/recent` — Get recent projects
- [[jira_get_projects_paginated]] — `GET /rest/api/3/project/search` — Get projects paginated ⭐
- [[jira_get_project]] — `GET /rest/api/3/project/{projectIdOrKey}` — Get project ⭐
- [[jira_update_project]] — `PUT /rest/api/3/project/{projectIdOrKey}` — Update project ✏️
- [[jira_delete_project]] — `DELETE /rest/api/3/project/{projectIdOrKey}` — Delete project ✏️
- [[jira_archive_project]] — `POST /rest/api/3/project/{projectIdOrKey}/archive` — Archive project ✏️
- [[jira_delete_project_asynchronously]] — `POST /rest/api/3/project/{projectIdOrKey}/delete` — Delete project asynchronously ✏️
- [[jira_restore_deleted_or_archived_project]] — `POST /rest/api/3/project/{projectIdOrKey}/restore` — Restore deleted or archived project ✏️
- [[jira_get_all_statuses_for_project]] — `GET /rest/api/3/project/{projectIdOrKey}/statuses` — Get all statuses for project
- [[jira_get_project_issue_type_hierarchy]] — `GET /rest/api/3/project/{projectId}/hierarchy` — Get project issue type hierarchy
- [[jira_get_project_notification_scheme]] — `GET /rest/api/3/project/{projectKeyOrId}/notificationscheme` — Get project notification scheme

## Screen schemes

- [[jira_get_screen_schemes]] — `GET /rest/api/3/screenscheme` — Get screen schemes
- [[jira_create_screen_scheme]] — `POST /rest/api/3/screenscheme` — Create screen scheme ✏️
- [[jira_update_screen_scheme]] — `PUT /rest/api/3/screenscheme/{screenSchemeId}` — Update screen scheme ✏️
- [[jira_delete_screen_scheme]] — `DELETE /rest/api/3/screenscheme/{screenSchemeId}` — Delete screen scheme ✏️

## Screen tab fields

- [[jira_get_all_screen_tab_fields]] — `GET /rest/api/3/screens/{screenId}/tabs/{tabId}/fields` — Get all screen tab fields
- [[jira_add_screen_tab_field]] — `POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields` — Add screen tab field ✏️
- [[jira_remove_screen_tab_field]] — `DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}` — Remove screen tab field ✏️
- [[jira_move_screen_tab_field]] — `POST /rest/api/3/screens/{screenId}/tabs/{tabId}/fields/{id}/move` — Move screen tab field ✏️

## Screen tabs

- [[jira_get_bulk_screen_tabs]] — `GET /rest/api/3/screens/tabs` — Get bulk screen tabs
- [[jira_get_all_screen_tabs]] — `GET /rest/api/3/screens/{screenId}/tabs` — Get all screen tabs
- [[jira_create_screen_tab]] — `POST /rest/api/3/screens/{screenId}/tabs` — Create screen tab ✏️
- [[jira_update_screen_tab]] — `PUT /rest/api/3/screens/{screenId}/tabs/{tabId}` — Update screen tab ✏️
- [[jira_delete_screen_tab]] — `DELETE /rest/api/3/screens/{screenId}/tabs/{tabId}` — Delete screen tab ✏️
- [[jira_move_screen_tab]] — `POST /rest/api/3/screens/{screenId}/tabs/{tabId}/move/{pos}` — Move screen tab ✏️

## Screens

- [[jira_get_screens_for_a_field]] — `GET /rest/api/3/field/{fieldId}/screens` — Get screens for a field
- [[jira_get_screens]] — `GET /rest/api/3/screens` — Get screens
- [[jira_create_screen]] — `POST /rest/api/3/screens` — Create screen ✏️
- [[jira_add_field_to_default_screen]] — `POST /rest/api/3/screens/addToDefault/{fieldId}` — Add field to default screen ✏️
- [[jira_update_screen]] — `PUT /rest/api/3/screens/{screenId}` — Update screen ✏️
- [[jira_delete_screen]] — `DELETE /rest/api/3/screens/{screenId}` — Delete screen ✏️
- [[jira_get_available_screen_fields]] — `GET /rest/api/3/screens/{screenId}/availableFields` — Get available screen fields

## Server info

- [[jira_get_jira_instance_info]] — `GET /rest/api/3/serverInfo` — Get Jira instance info

## Service Registry

- [[Jira v3 - Retrieve the attributes of service registries]] — `GET /rest/atlassian-connect/1/service-registry` — Retrieve the attributes of service registries 🔒

## Status

- [[jira_bulk_get_statuses]] — `GET /rest/api/3/statuses` — Bulk get statuses
- [[jira_bulk_update_statuses]] — `PUT /rest/api/3/statuses` — Bulk update statuses ✏️
- [[jira_bulk_create_statuses]] — `POST /rest/api/3/statuses` — Bulk create statuses ✏️
- [[jira_bulk_delete_statuses]] — `DELETE /rest/api/3/statuses` — Bulk delete Statuses ✏️
- [[jira_bulk_get_statuses_by_name]] — `GET /rest/api/3/statuses/byNames` — Bulk get statuses by name
- [[jira_search_statuses_paginated]] — `GET /rest/api/3/statuses/search` — Search statuses paginated
- [[jira_get_issue_type_usages_by_status_and_project]] — `GET /rest/api/3/statuses/{statusId}/project/{projectId}/issueTypeUsages` — Get issue type usages by status and project
- [[jira_get_project_usages_by_status]] — `GET /rest/api/3/statuses/{statusId}/projectUsages` — Get project usages by status
- [[jira_get_workflow_usages_by_status]] — `GET /rest/api/3/statuses/{statusId}/workflowUsages` — Get workflow usages by status

## Tasks

- [[jira_get_task]] — `GET /rest/api/3/task/{taskId}` — Get task
- [[jira_cancel_task]] — `POST /rest/api/3/task/{taskId}/cancel` — Cancel task ✏️

## Teams in plan

- [[jira_get_teams_in_plan_paginated]] — `GET /rest/api/3/plans/plan/{planId}/team` — Get teams in plan paginated
- [[jira_add_atlassian_team_to_plan]] — `POST /rest/api/3/plans/plan/{planId}/team/atlassian` — Add Atlassian team to plan ✏️
- [[jira_get_atlassian_team_in_plan]] — `GET /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}` — Get Atlassian team in plan
- [[jira_update_atlassian_team_in_plan]] — `PUT /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}` — Update Atlassian team in plan ✏️
- [[jira_remove_atlassian_team_from_plan]] — `DELETE /rest/api/3/plans/plan/{planId}/team/atlassian/{atlassianTeamId}` — Remove Atlassian team from plan ✏️
- [[jira_create_plan_only_team]] — `POST /rest/api/3/plans/plan/{planId}/team/planonly` — Create plan-only team ✏️
- [[jira_get_plan_only_team]] — `GET /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}` — Get plan-only team
- [[jira_update_plan_only_team]] — `PUT /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}` — Update plan-only team ✏️
- [[jira_delete_plan_only_team]] — `DELETE /rest/api/3/plans/plan/{planId}/team/planonly/{planOnlyTeamId}` — Delete plan-only team ✏️

## Time tracking

- [[jira_get_selected_time_tracking_provider]] — `GET /rest/api/3/configuration/timetracking` — Get selected time tracking provider
- [[jira_select_time_tracking_provider]] — `PUT /rest/api/3/configuration/timetracking` — Select time tracking provider ✏️
- [[jira_get_all_time_tracking_providers]] — `GET /rest/api/3/configuration/timetracking/list` — Get all time tracking providers
- [[jira_get_time_tracking_settings]] — `GET /rest/api/3/configuration/timetracking/options` — Get time tracking settings
- [[jira_set_time_tracking_settings]] — `PUT /rest/api/3/configuration/timetracking/options` — Set time tracking settings ✏️

## UI modifications (apps)

- [[Jira v3 - Get UI modifications]] — `GET /rest/api/3/uiModifications` — Get UI modifications 🔒
- [[Jira v3 - Create UI modification]] — `POST /rest/api/3/uiModifications` — Create UI modification ✏️🔒
- [[Jira v3 - Update UI modification]] — `PUT /rest/api/3/uiModifications/{uiModificationId}` — Update UI modification ✏️🔒
- [[Jira v3 - Delete UI modification]] — `DELETE /rest/api/3/uiModifications/{uiModificationId}` — Delete UI modification ✏️🔒

## User properties

- [[jira_get_user_property_keys]] — `GET /rest/api/3/user/properties` — Get user property keys
- [[jira_get_user_property]] — `GET /rest/api/3/user/properties/{propertyKey}` — Get user property
- [[jira_set_user_property]] — `PUT /rest/api/3/user/properties/{propertyKey}` — Set user property ✏️
- [[jira_delete_user_property]] — `DELETE /rest/api/3/user/properties/{propertyKey}` — Delete user property ✏️

## User search

- [[jira_find_users_assignable_to_projects]] — `GET /rest/api/3/user/assignable/multiProjectSearch` — Find users assignable to projects
- [[jira_find_users_assignable_to_issues]] — `GET /rest/api/3/user/assignable/search` — Find users assignable to issues
- [[jira_find_users_with_permissions]] — `GET /rest/api/3/user/permission/search` — Find users with permissions
- [[jira_find_users_for_picker]] — `GET /rest/api/3/user/picker` — Find users for picker
- [[jira_find_users]] — `GET /rest/api/3/user/search` — Find users ⭐
- [[jira_find_users_by_query]] — `GET /rest/api/3/user/search/query` — Find users by query
- [[jira_find_user_keys_by_query]] — `GET /rest/api/3/user/search/query/key` — Find user keys by query
- [[jira_find_users_with_browse_permission]] — `GET /rest/api/3/user/viewissue/search` — Find users with browse permission

## Users

- [[jira_get_user]] — `GET /rest/api/3/user` — Get user
- [[jira_delete_user]] — `DELETE /rest/api/3/user` — Delete user ✏️
- [[jira_bulk_get_users]] — `GET /rest/api/3/user/bulk` — Bulk get users
- [[jira_get_account_ids_for_users]] — `GET /rest/api/3/user/bulk/migration` — Get account IDs for users
- [[jira_get_user_default_columns]] — `GET /rest/api/3/user/columns` — Get user default columns
- [[Jira v3 - Set user default columns]] — `PUT /rest/api/3/user/columns` — Set user default columns ✏️📎
- [[jira_reset_user_default_columns]] — `DELETE /rest/api/3/user/columns` — Reset user default columns ✏️
- [[Jira v3 - Get user email]] — `GET /rest/api/3/user/email` — Get user email 🔒
- [[Jira v3 - Get user email bulk]] — `GET /rest/api/3/user/email/bulk` — Get user email bulk 🔒
- [[jira_get_user_groups]] — `GET /rest/api/3/user/groups` — Get user groups
- [[jira_get_all_users_default]] — `GET /rest/api/3/users` — Get all users default
- [[jira_get_all_users]] — `GET /rest/api/3/users/search` — Get all users

## Webhooks

- [[jira_get_dynamic_webhooks_for_app]] — `GET /rest/api/3/webhook` — Get dynamic webhooks for app
- [[jira_register_dynamic_webhooks]] — `POST /rest/api/3/webhook` — Register dynamic webhooks ✏️
- [[jira_delete_webhooks_by_id]] — `DELETE /rest/api/3/webhook` — Delete webhooks by ID ✏️
- [[jira_get_failed_webhooks]] — `GET /rest/api/3/webhook/failed` — Get failed webhooks
- [[jira_extend_webhook_life]] — `PUT /rest/api/3/webhook/refresh` — Extend webhook life ✏️

## Workflow scheme drafts

- [[jira_create_draft_workflow_scheme]] — `POST /rest/api/3/workflowscheme/{id}/createdraft` — Create draft workflow scheme ✏️
- [[jira_get_draft_workflow_scheme]] — `GET /rest/api/3/workflowscheme/{id}/draft` — Get draft workflow scheme
- [[jira_update_draft_workflow_scheme]] — `PUT /rest/api/3/workflowscheme/{id}/draft` — Update draft workflow scheme ✏️
- [[jira_delete_draft_workflow_scheme]] — `DELETE /rest/api/3/workflowscheme/{id}/draft` — Delete draft workflow scheme ✏️
- [[jira_get_draft_default_workflow]] — `GET /rest/api/3/workflowscheme/{id}/draft/default` — Get draft default workflow
- [[jira_update_draft_default_workflow]] — `PUT /rest/api/3/workflowscheme/{id}/draft/default` — Update draft default workflow ✏️
- [[jira_delete_draft_default_workflow]] — `DELETE /rest/api/3/workflowscheme/{id}/draft/default` — Delete draft default workflow ✏️
- [[jira_get_workflow_for_issue_type_in_draft_workflow_scheme]] — `GET /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}` — Get workflow for issue type in draft workflow scheme
- [[jira_set_workflow_for_issue_type_in_draft_workflow_scheme]] — `PUT /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}` — Set workflow for issue type in draft workflow scheme ✏️
- [[jira_delete_workflow_for_issue_type_in_draft_workflow_scheme]] — `DELETE /rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}` — Delete workflow for issue type in draft workflow scheme ✏️
- [[jira_publish_draft_workflow_scheme]] — `POST /rest/api/3/workflowscheme/{id}/draft/publish` — Publish draft workflow scheme ✏️
- [[jira_get_issue_types_for_workflows_in_draft_workflow_scheme]] — `GET /rest/api/3/workflowscheme/{id}/draft/workflow` — Get issue types for workflows in draft workflow scheme
- [[jira_set_issue_types_for_workflow_in_workflow_scheme]] — `PUT /rest/api/3/workflowscheme/{id}/draft/workflow` — Set issue types for workflow in workflow scheme ✏️
- [[jira_delete_issue_types_for_workflow_in_draft_workflow_scheme]] — `DELETE /rest/api/3/workflowscheme/{id}/draft/workflow` — Delete issue types for workflow in draft workflow scheme ✏️

## Workflow scheme project associations

- [[jira_get_workflow_scheme_project_associations]] — `GET /rest/api/3/workflowscheme/project` — Get workflow scheme project associations
- [[jira_assign_workflow_scheme_to_project]] — `PUT /rest/api/3/workflowscheme/project` — Assign workflow scheme to project ✏️

## Workflow schemes

- [[jira_get_all_workflow_schemes]] — `GET /rest/api/3/workflowscheme` — Get all workflow schemes
- [[jira_create_workflow_scheme]] — `POST /rest/api/3/workflowscheme` — Create workflow scheme ✏️
- [[jira_switch_workflow_scheme_for_project]] — `POST /rest/api/3/workflowscheme/project/switch` — Switch workflow scheme for project ✏️
- [[jira_bulk_get_workflow_schemes]] — `POST /rest/api/3/workflowscheme/read` — Bulk get workflow schemes
- [[jira_update_workflow_scheme]] — `POST /rest/api/3/workflowscheme/update` — Update workflow scheme ✏️
- [[jira_get_required_status_mappings_for_workflow_scheme_update]] — `POST /rest/api/3/workflowscheme/update/mappings` — Get required status mappings for workflow scheme update
- [[jira_get_workflow_scheme]] — `GET /rest/api/3/workflowscheme/{id}` — Get workflow scheme
- [[jira_classic_update_workflow_scheme]] — `PUT /rest/api/3/workflowscheme/{id}` — Classic update workflow scheme ✏️
- [[jira_delete_workflow_scheme]] — `DELETE /rest/api/3/workflowscheme/{id}` — Delete workflow scheme ✏️
- [[jira_get_default_workflow]] — `GET /rest/api/3/workflowscheme/{id}/default` — Get default workflow
- [[jira_update_default_workflow]] — `PUT /rest/api/3/workflowscheme/{id}/default` — Update default workflow ✏️
- [[jira_delete_default_workflow]] — `DELETE /rest/api/3/workflowscheme/{id}/default` — Delete default workflow ✏️
- [[jira_get_workflow_for_issue_type_in_workflow_scheme]] — `GET /rest/api/3/workflowscheme/{id}/issuetype/{issueType}` — Get workflow for issue type in workflow scheme
- [[jira_set_workflow_for_issue_type_in_workflow_scheme]] — `PUT /rest/api/3/workflowscheme/{id}/issuetype/{issueType}` — Set workflow for issue type in workflow scheme ✏️
- [[jira_delete_workflow_for_issue_type_in_workflow_scheme]] — `DELETE /rest/api/3/workflowscheme/{id}/issuetype/{issueType}` — Delete workflow for issue type in workflow scheme ✏️
- [[jira_get_issue_types_for_workflows_in_workflow_scheme]] — `GET /rest/api/3/workflowscheme/{id}/workflow` — Get issue types for workflows in workflow scheme
- [[jira_set_issue_types_for_workflow_in_workflow_scheme_put]] — `PUT /rest/api/3/workflowscheme/{id}/workflow` — Set issue types for workflow in workflow scheme ✏️
- [[jira_delete_issue_types_for_workflow_in_workflow_scheme]] — `DELETE /rest/api/3/workflowscheme/{id}/workflow` — Delete issue types for workflow in workflow scheme ✏️
- [[jira_get_projects_which_are_using_a_given_workflow_scheme]] — `GET /rest/api/3/workflowscheme/{workflowSchemeId}/projectUsages` — Get projects which are using a given workflow scheme

## Workflow status categories

- [[jira_get_all_status_categories]] — `GET /rest/api/3/statuscategory` — Get all status categories
- [[jira_get_status_category]] — `GET /rest/api/3/statuscategory/{idOrKey}` — Get status category

## Workflow statuses

- [[jira_get_all_statuses]] — `GET /rest/api/3/status` — Get all statuses
- [[jira_get_status]] — `GET /rest/api/3/status/{idOrName}` — Get status

## Workflow transition rules

- [[jira_get_workflow_transition_rule_configurations]] — `GET /rest/api/3/workflow/rule/config` — Get workflow transition rule configurations
- [[jira_update_workflow_transition_rule_configurations]] — `PUT /rest/api/3/workflow/rule/config` — Update workflow transition rule configurations ✏️
- [[Jira v3 - Delete workflow transition rule configurations]] — `PUT /rest/api/3/workflow/rule/config/delete` — Delete workflow transition rule configurations ✏️🔒

## Workflows

- [[jira_read_workflow_version_from_history]] — `POST /rest/api/3/workflow/history` — Read workflow version from history ✏️
- [[jira_list_workflow_history_entries]] — `POST /rest/api/3/workflow/history/list` — List workflow history entries
- [[jira_get_workflows_paginated]] — `GET /rest/api/3/workflow/search` — Get workflows paginated
- [[jira_delete_inactive_workflow]] — `DELETE /rest/api/3/workflow/{entityId}` — Delete inactive workflow ✏️
- [[jira_get_issue_types_in_a_project_that_are_using_a_given_workflo]] — `GET /rest/api/3/workflow/{workflowId}/project/{projectId}/issueTypeUsages` — Get issue types in a project that are using a given workflow
- [[jira_get_projects_using_a_given_workflow]] — `GET /rest/api/3/workflow/{workflowId}/projectUsages` — Get projects using a given workflow
- [[jira_get_workflow_schemes_which_are_using_a_given_workflow]] — `GET /rest/api/3/workflow/{workflowId}/workflowSchemes` — Get workflow schemes which are using a given workflow
- [[jira_bulk_get_workflows]] — `POST /rest/api/3/workflows` — Bulk get workflows
- [[jira_get_available_workflow_capabilities]] — `GET /rest/api/3/workflows/capabilities` — Get available workflow capabilities
- [[jira_copy_workflow]] — `POST /rest/api/3/workflows/copy` — Copy workflow ✏️
- [[jira_bulk_create_workflows]] — `POST /rest/api/3/workflows/create` — Bulk create workflows ✏️
- [[jira_validate_create_workflows]] — `POST /rest/api/3/workflows/create/validation` — Validate create workflows ✏️
- [[jira_get_the_user_s_default_workflow_editor]] — `GET /rest/api/3/workflows/defaultEditor` — Get the user's default workflow editor
- [[jira_preview_workflow]] — `POST /rest/api/3/workflows/preview` — Preview workflow ✏️
- [[jira_search_workflows]] — `GET /rest/api/3/workflows/search` — Search workflows
- [[jira_bulk_update_workflows]] — `POST /rest/api/3/workflows/update` — Bulk update workflows ✏️
- [[jira_validate_update_workflows]] — `POST /rest/api/3/workflows/update/validation` — Validate update workflows

## Other operations

- [[jira_get_worklogs_by_issue_id_and_worklog_id]] — `POST /rest/internal/api/latest/worklog/bulk` — Get worklogs by issue id and worklog id
