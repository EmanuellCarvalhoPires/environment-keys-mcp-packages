---
tags:
  - moc
  - mcp
  - api/app/confluence
up: "[[MCP Tools]]"
---
# MCP - Confluence v2

- **Tools:** 218 (exposed: 7; the others via `run_vault_tool`)
- **Requests only:** 0
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/confluence/rest/v2/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Admin Key

- [[confluence_get_admin_key]] — `GET /admin-key` — Get Admin Key
- [[confluence_enable_admin_key]] — `POST /admin-key` — Enable Admin Key ✏️
- [[confluence_disable_admin_key]] — `DELETE /admin-key` — Disable Admin Key ✏️

## Attachment

- [[confluence_get_attachments]] — `GET /attachments` — Get attachments
- [[confluence_get_attachment_by_id]] — `GET /attachments/{id}` — Get attachment by id
- [[confluence_delete_attachment]] — `DELETE /attachments/{id}` — Delete attachment ✏️
- [[confluence_get_attachments_for_blog_post]] — `GET /blogposts/{id}/attachments` — Get attachments for blog post
- [[confluence_get_attachments_for_custom_content]] — `GET /custom-content/{id}/attachments` — Get attachments for custom content
- [[confluence_get_attachments_for_label]] — `GET /labels/{id}/attachments` — Get attachments for label
- [[confluence_get_attachments_for_page]] — `GET /pages/{id}/attachments` — Get attachments for page
- [[confluence_download_attachment_thumbnail_by_id]] — `GET /attachments/{id}/thumbnail/download` — Download attachment thumbnail by id

## App Properties

- [[confluence_get_forge_app_properties]] — `GET /app/properties` — Get Forge app properties.
- [[confluence_get_a_forge_app_property_by_key]] — `GET /app/properties/{propertyKey}` — Get a Forge app property by key.
- [[confluence_create_or_update_a_forge_app_property]] — `PUT /app/properties/{propertyKey}` — Create or update a Forge app property. ✏️
- [[confluence_deletes_a_forge_app_property]] — `DELETE /app/properties/{propertyKey}` — Deletes a Forge app property. ✏️

## Ancestors

- [[confluence_get_all_ancestors_of_whiteboard]] — `GET /whiteboards/{id}/ancestors` — Get all ancestors of whiteboard
- [[confluence_get_all_ancestors_of_database]] — `GET /databases/{id}/ancestors` — Get all ancestors of database
- [[confluence_get_all_ancestors_of_smart_link_in_content_tree]] — `GET /embeds/{id}/ancestors` — Get all ancestors of Smart Link in content tree
- [[confluence_get_all_ancestors_of_folder]] — `GET /folders/{id}/ancestors` — Get all ancestors of folder
- [[confluence_get_all_ancestors_of_page]] — `GET /pages/{id}/ancestors` — Get all ancestors of page

## Blog Post

- [[confluence_get_blog_posts]] — `GET /blogposts` — Get blog posts
- [[confluence_create_blog_post]] — `POST /blogposts` — Create blog post ✏️
- [[confluence_get_blog_post_by_id]] — `GET /blogposts/{id}` — Get blog post by id
- [[confluence_update_blog_post]] — `PUT /blogposts/{id}` — Update blog post ✏️
- [[confluence_delete_blog_post]] — `DELETE /blogposts/{id}` — Delete blog post ✏️
- [[confluence_get_blog_posts_for_label]] — `GET /labels/{id}/blogposts` — Get blog posts for label
- [[confluence_get_blog_posts_in_space]] — `GET /spaces/{id}/blogposts` — Get blog posts in space

## Children

- [[confluence_get_direct_children_of_a_whiteboard]] — `GET /whiteboards/{id}/direct-children` — Get direct children of a whiteboard
- [[confluence_get_direct_children_of_a_database]] — `GET /databases/{id}/direct-children` — Get direct children of a database
- [[confluence_get_direct_children_of_a_smart_link]] — `GET /embeds/{id}/direct-children` — Get direct children of a Smart Link
- [[confluence_get_direct_children_of_a_folder]] — `GET /folders/{id}/direct-children` — Get direct children of a folder
- [[confluence_get_child_pages]] — `GET /pages/{id}/children` — Get child pages
- [[confluence_get_child_custom_content]] — `GET /custom-content/{id}/children` — Get child custom content
- [[confluence_get_direct_children_of_a_page]] — `GET /pages/{id}/direct-children` — Get direct children of a page

## Classification Level

- [[confluence_get_list_of_classification_levels]] — `GET /classification-levels` — Get list of classification levels
- [[confluence_get_space_default_classification_level]] — `GET /spaces/{id}/classification-level/default` — Get space default classification level
- [[confluence_update_space_default_classification_level]] — `PUT /spaces/{id}/classification-level/default` — Update space default classification level ✏️
- [[confluence_delete_space_default_classification_level]] — `DELETE /spaces/{id}/classification-level/default` — Delete space default classification level ✏️
- [[confluence_get_page_classification_level]] — `GET /pages/{id}/classification-level` — Get page classification level
- [[confluence_update_page_classification_level]] — `PUT /pages/{id}/classification-level` — Update page classification level ✏️
- [[confluence_reset_page_classification_level]] — `POST /pages/{id}/classification-level/reset` — Reset page classification level ✏️
- [[confluence_get_blog_post_classification_level]] — `GET /blogposts/{id}/classification-level` — Get blog post classification level
- [[confluence_update_blog_post_classification_level]] — `PUT /blogposts/{id}/classification-level` — Update blog post classification level ✏️
- [[confluence_reset_blog_post_classification_level]] — `POST /blogposts/{id}/classification-level/reset` — Reset blog post classification level ✏️
- [[confluence_get_whiteboard_classification_level]] — `GET /whiteboards/{id}/classification-level` — Get whiteboard classification level
- [[confluence_update_whiteboard_classification_level]] — `PUT /whiteboards/{id}/classification-level` — Update whiteboard classification level ✏️
- [[confluence_reset_whiteboard_classification_level]] — `POST /whiteboards/{id}/classification-level/reset` — Reset whiteboard classification level ✏️
- [[confluence_get_database_classification_level]] — `GET /databases/{id}/classification-level` — Get database classification level
- [[confluence_update_database_classification_level]] — `PUT /databases/{id}/classification-level` — Update database classification level ✏️
- [[confluence_reset_database_classification_level]] — `POST /databases/{id}/classification-level/reset` — Reset database classification level ✏️

## Comment

- [[confluence_get_attachment_comments]] — `GET /attachments/{id}/footer-comments` — Get attachment comments
- [[confluence_get_custom_content_comments]] — `GET /custom-content/{id}/footer-comments` — Get custom content comments
- [[confluence_get_footer_comments_for_page]] — `GET /pages/{id}/footer-comments` — Get footer comments for page ⭐
- [[confluence_get_inline_comments_for_page]] — `GET /pages/{id}/inline-comments` — Get inline comments for page
- [[confluence_get_footer_comments_for_blog_post]] — `GET /blogposts/{id}/footer-comments` — Get footer comments for blog post
- [[confluence_get_inline_comments_for_blog_post]] — `GET /blogposts/{id}/inline-comments` — Get inline comments for blog post
- [[confluence_get_footer_comments]] — `GET /footer-comments` — Get footer comments
- [[confluence_create_footer_comment]] — `POST /footer-comments` — Create footer comment ✏️
- [[confluence_get_footer_comment_by_id]] — `GET /footer-comments/{comment-id}` — Get footer comment by id
- [[confluence_update_footer_comment]] — `PUT /footer-comments/{comment-id}` — Update footer comment ✏️
- [[confluence_delete_footer_comment]] — `DELETE /footer-comments/{comment-id}` — Delete footer comment ✏️
- [[confluence_get_children_footer_comments]] — `GET /footer-comments/{id}/children` — Get children footer comments
- [[confluence_get_inline_comments]] — `GET /inline-comments` — Get inline comments
- [[confluence_create_inline_comment]] — `POST /inline-comments` — Create inline comment ✏️
- [[confluence_get_inline_comment_by_id]] — `GET /inline-comments/{comment-id}` — Get inline comment by id
- [[confluence_update_inline_comment]] — `PUT /inline-comments/{comment-id}` — Update inline comment ✏️
- [[confluence_delete_inline_comment]] — `DELETE /inline-comments/{comment-id}` — Delete inline comment ✏️
- [[confluence_get_children_inline_comments]] — `GET /inline-comments/{id}/children` — Get children inline comments

## Content

- [[confluence_convert_content_ids_to_content_types]] — `POST /content/convert-ids-to-types` — Convert content ids to content types

## Content Properties

- [[confluence_get_content_properties_for_attachment]] — `GET /attachments/{attachment-id}/properties` — Get content properties for attachment
- [[confluence_create_content_property_for_attachment]] — `POST /attachments/{attachment-id}/properties` — Create content property for attachment ✏️
- [[confluence_get_content_property_for_attachment_by_id]] — `GET /attachments/{attachment-id}/properties/{property-id}` — Get content property for attachment by id
- [[confluence_update_content_property_for_attachment_by_id]] — `PUT /attachments/{attachment-id}/properties/{property-id}` — Update content property for attachment by id ✏️
- [[confluence_delete_content_property_for_attachment_by_id]] — `DELETE /attachments/{attachment-id}/properties/{property-id}` — Delete content property for attachment by id ✏️
- [[confluence_get_content_properties_for_blog_post]] — `GET /blogposts/{blogpost-id}/properties` — Get content properties for blog post
- [[confluence_create_content_property_for_blog_post]] — `POST /blogposts/{blogpost-id}/properties` — Create content property for blog post ✏️
- [[confluence_get_content_property_for_blog_post_by_id]] — `GET /blogposts/{blogpost-id}/properties/{property-id}` — Get content property for blog post by id
- [[confluence_update_content_property_for_blog_post_by_id]] — `PUT /blogposts/{blogpost-id}/properties/{property-id}` — Update content property for blog post by id ✏️
- [[confluence_delete_content_property_for_blogpost_by_id]] — `DELETE /blogposts/{blogpost-id}/properties/{property-id}` — Delete content property for blogpost by id ✏️
- [[confluence_get_content_properties_for_custom_content]] — `GET /custom-content/{custom-content-id}/properties` — Get content properties for custom content
- [[confluence_create_content_property_for_custom_content]] — `POST /custom-content/{custom-content-id}/properties` — Create content property for custom content ✏️
- [[confluence_get_content_property_for_custom_content_by_id]] — `GET /custom-content/{custom-content-id}/properties/{property-id}` — Get content property for custom content by id
- [[confluence_update_content_property_for_custom_content_by_id]] — `PUT /custom-content/{custom-content-id}/properties/{property-id}` — Update content property for custom content by id ✏️
- [[confluence_delete_content_property_for_custom_content_by_id]] — `DELETE /custom-content/{custom-content-id}/properties/{property-id}` — Delete content property for custom content by id ✏️
- [[confluence_get_content_properties_for_page]] — `GET /pages/{page-id}/properties` — Get content properties for page
- [[confluence_create_content_property_for_page]] — `POST /pages/{page-id}/properties` — Create content property for page ✏️
- [[confluence_get_content_property_for_page_by_id]] — `GET /pages/{page-id}/properties/{property-id}` — Get content property for page by id
- [[confluence_update_content_property_for_page_by_id]] — `PUT /pages/{page-id}/properties/{property-id}` — Update content property for page by id ✏️
- [[confluence_delete_content_property_for_page_by_id]] — `DELETE /pages/{page-id}/properties/{property-id}` — Delete content property for page by id ✏️
- [[confluence_get_content_properties_for_whiteboard]] — `GET /whiteboards/{id}/properties` — Get content properties for whiteboard
- [[confluence_create_content_property_for_whiteboard]] — `POST /whiteboards/{id}/properties` — Create content property for whiteboard ✏️
- [[confluence_get_content_property_for_whiteboard_by_id]] — `GET /whiteboards/{whiteboard-id}/properties/{property-id}` — Get content property for whiteboard by id
- [[confluence_update_content_property_for_whiteboard_by_id]] — `PUT /whiteboards/{whiteboard-id}/properties/{property-id}` — Update content property for whiteboard by id ✏️
- [[confluence_delete_content_property_for_whiteboard_by_id]] — `DELETE /whiteboards/{whiteboard-id}/properties/{property-id}` — Delete content property for whiteboard by id ✏️
- [[confluence_get_content_properties_for_database]] — `GET /databases/{id}/properties` — Get content properties for database
- [[confluence_create_content_property_for_database]] — `POST /databases/{id}/properties` — Create content property for database ✏️
- [[confluence_get_content_property_for_database_by_id]] — `GET /databases/{database-id}/properties/{property-id}` — Get content property for database by id
- [[confluence_update_content_property_for_database_by_id]] — `PUT /databases/{database-id}/properties/{property-id}` — Update content property for database by id ✏️
- [[confluence_delete_content_property_for_database_by_id]] — `DELETE /databases/{database-id}/properties/{property-id}` — Delete content property for database by id ✏️
- [[confluence_get_content_properties_for_smart_link_in_the_content]] — `GET /embeds/{id}/properties` — Get content properties for Smart Link in the content tree
- [[confluence_create_content_property_for_smart_link_in_the_content]] — `POST /embeds/{id}/properties` — Create content property for Smart Link in the content tree ✏️
- [[confluence_get_content_property_for_smart_link_in_the_content_tr]] — `GET /embeds/{embed-id}/properties/{property-id}` — Get content property for Smart Link in the content tree by id
- [[confluence_update_content_property_for_smart_link_in_the_content]] — `PUT /embeds/{embed-id}/properties/{property-id}` — Update content property for Smart Link in the content tree by id ✏️
- [[confluence_delete_content_property_for_smart_link_in_the_content]] — `DELETE /embeds/{embed-id}/properties/{property-id}` — Delete content property for Smart Link in the content tree by id ✏️
- [[confluence_get_content_properties_for_folder]] — `GET /folders/{id}/properties` — Get content properties for folder
- [[confluence_create_content_property_for_folder]] — `POST /folders/{id}/properties` — Create content property for folder ✏️
- [[confluence_get_content_property_for_folder_by_id]] — `GET /folders/{folder-id}/properties/{property-id}` — Get content property for folder by id
- [[confluence_update_content_property_for_folder_by_id]] — `PUT /folders/{folder-id}/properties/{property-id}` — Update content property for folder by id ✏️
- [[confluence_delete_content_property_for_folder_by_id]] — `DELETE /folders/{folder-id}/properties/{property-id}` — Delete content property for folder by id ✏️
- [[confluence_get_content_properties_for_comment]] — `GET /comments/{comment-id}/properties` — Get content properties for comment
- [[confluence_create_content_property_for_comment]] — `POST /comments/{comment-id}/properties` — Create content property for comment ✏️
- [[confluence_get_content_property_for_comment_by_id]] — `GET /comments/{comment-id}/properties/{property-id}` — Get content property for comment by id
- [[confluence_update_content_property_for_comment_by_id]] — `PUT /comments/{comment-id}/properties/{property-id}` — Update content property for comment by id ✏️
- [[confluence_delete_content_property_for_comment_by_id]] — `DELETE /comments/{comment-id}/properties/{property-id}` — Delete content property for comment by id ✏️

## Custom Content

- [[confluence_get_custom_content_by_type_in_blog_post]] — `GET /blogposts/{id}/custom-content` — Get custom content by type in blog post
- [[confluence_get_custom_content_by_type]] — `GET /custom-content` — Get custom content by type
- [[confluence_create_custom_content]] — `POST /custom-content` — Create custom content ✏️
- [[confluence_get_custom_content_by_id]] — `GET /custom-content/{id}` — Get custom content by id
- [[confluence_update_custom_content]] — `PUT /custom-content/{id}` — Update custom content ✏️
- [[confluence_delete_custom_content]] — `DELETE /custom-content/{id}` — Delete custom content ✏️
- [[confluence_get_custom_content_by_type_in_page]] — `GET /pages/{id}/custom-content` — Get custom content by type in page
- [[confluence_get_custom_content_by_type_in_space]] — `GET /spaces/{id}/custom-content` — Get custom content by type in space

## Database

- [[confluence_create_database]] — `POST /databases` — Create database ✏️
- [[confluence_get_database_by_id]] — `GET /databases/{id}` — Get database by id
- [[confluence_delete_database]] — `DELETE /databases/{id}` — Delete database ✏️

## Data Policies

- [[confluence_get_data_policy_metadata_for_the_workspace]] — `GET /data-policies/metadata` — Get data policy metadata for the workspace
- [[confluence_get_spaces_with_data_policies]] — `GET /data-policies/spaces` — Get spaces with data policies

## Descendants

- [[confluence_get_descendants_of_a_whiteboard]] — `GET /whiteboards/{id}/descendants` — Get descendants of a whiteboard
- [[confluence_get_descendants_of_a_database]] — `GET /databases/{id}/descendants` — Get descendants of a database
- [[confluence_get_descendants_of_a_smart_link]] — `GET /embeds/{id}/descendants` — Get descendants of a smart link
- [[confluence_get_descendants_of_folder]] — `GET /folders/{id}/descendants` — Get descendants of folder
- [[confluence_get_descendants_of_page]] — `GET /pages/{id}/descendants` — Get descendants of page

## Folder

- [[confluence_create_folder]] — `POST /folders` — Create folder ✏️
- [[confluence_get_folder_by_id]] — `GET /folders/{id}` — Get folder by id
- [[confluence_delete_folder]] — `DELETE /folders/{id}` — Delete folder ✏️

## Label

- [[confluence_get_labels_for_attachment]] — `GET /attachments/{id}/labels` — Get labels for attachment
- [[confluence_get_labels_for_blog_post]] — `GET /blogposts/{id}/labels` — Get labels for blog post
- [[confluence_get_labels_for_custom_content]] — `GET /custom-content/{id}/labels` — Get labels for custom content
- [[confluence_get_labels]] — `GET /labels` — Get labels
- [[confluence_get_labels_for_page]] — `GET /pages/{id}/labels` — Get labels for page
- [[confluence_get_labels_for_space]] — `GET /spaces/{id}/labels` — Get labels for space
- [[confluence_get_labels_for_space_content]] — `GET /spaces/{id}/content/labels` — Get labels for space content

## Like

- [[confluence_get_like_count_for_blog_post]] — `GET /blogposts/{id}/likes/count` — Get like count for blog post
- [[confluence_get_account_ids_of_likes_for_blog_post]] — `GET /blogposts/{id}/likes/users` — Get account IDs of likes for blog post
- [[confluence_get_like_count_for_page]] — `GET /pages/{id}/likes/count` — Get like count for page
- [[confluence_get_account_ids_of_likes_for_page]] — `GET /pages/{id}/likes/users` — Get account IDs of likes for page
- [[confluence_get_like_count_for_footer_comment]] — `GET /footer-comments/{id}/likes/count` — Get like count for footer comment
- [[confluence_get_account_ids_of_likes_for_footer_comment]] — `GET /footer-comments/{id}/likes/users` — Get account IDs of likes for footer comment
- [[confluence_get_like_count_for_inline_comment]] — `GET /inline-comments/{id}/likes/count` — Get like count for inline comment
- [[confluence_get_account_ids_of_likes_for_inline_comment]] — `GET /inline-comments/{id}/likes/users` — Get account IDs of likes for inline comment

## Operation

- [[confluence_get_permitted_operations_for_attachment]] — `GET /attachments/{id}/operations` — Get permitted operations for attachment
- [[confluence_get_permitted_operations_for_blog_post]] — `GET /blogposts/{id}/operations` — Get permitted operations for blog post
- [[confluence_get_permitted_operations_for_custom_content]] — `GET /custom-content/{id}/operations` — Get permitted operations for custom content
- [[confluence_get_permitted_operations_for_page]] — `GET /pages/{id}/operations` — Get permitted operations for page
- [[confluence_get_permitted_operations_for_a_whiteboard]] — `GET /whiteboards/{id}/operations` — Get permitted operations for a whiteboard
- [[confluence_get_permitted_operations_for_a_database]] — `GET /databases/{id}/operations` — Get permitted operations for a database
- [[confluence_get_permitted_operations_for_a_smart_link_in_the_cont]] — `GET /embeds/{id}/operations` — Get permitted operations for a Smart Link in the content tree
- [[confluence_get_permitted_operations_for_a_folder]] — `GET /folders/{id}/operations` — Get permitted operations for a folder
- [[confluence_get_permitted_operations_for_space]] — `GET /spaces/{id}/operations` — Get permitted operations for space
- [[confluence_get_permitted_operations_for_footer_comment]] — `GET /footer-comments/{id}/operations` — Get permitted operations for footer comment
- [[confluence_get_permitted_operations_for_inline_comment]] — `GET /inline-comments/{id}/operations` — Get permitted operations for inline comment

## Page

- [[confluence_get_pages_for_label]] — `GET /labels/{id}/pages` — Get pages for label
- [[confluence_get_pages]] — `GET /pages` — Get pages ⭐
- [[confluence_create_page]] — `POST /pages` — Create page ✏️⭐
- [[confluence_get_page_by_id]] — `GET /pages/{id}` — Get page by id ⭐
- [[confluence_update_page]] — `PUT /pages/{id}` — Update page ✏️⭐
- [[confluence_delete_page]] — `DELETE /pages/{id}` — Delete page ✏️
- [[confluence_update_page_title]] — `PUT /pages/{id}/title` — Update page title ✏️
- [[confluence_get_pages_in_space]] — `GET /spaces/{id}/pages` — Get pages in space ⭐

## Redactions

- [[confluence_redact_content_in_a_confluence_page]] — `POST /pages/{id}/redact` — Redact Content in a Confluence Page ✏️
- [[confluence_redact_content_in_a_confluence_blog_post]] — `POST /blogposts/{id}/redact` — Redact Content in a Confluence Blog Post ✏️

## Smart Link

- [[confluence_create_smart_link_in_the_content_tree]] — `POST /embeds` — Create Smart Link in the content tree ✏️
- [[confluence_get_smart_link_in_the_content_tree_by_id]] — `GET /embeds/{id}` — Get Smart Link in the content tree by id
- [[confluence_delete_smart_link_in_the_content_tree]] — `DELETE /embeds/{id}` — Delete Smart Link in the content tree ✏️

## Space

- [[confluence_get_spaces]] — `GET /spaces` — Get spaces ⭐
- [[confluence_create_space]] — `POST /spaces` — Create space ✏️
- [[confluence_get_space_by_id]] — `GET /spaces/{id}` — Get space by id

## Space Permissions

- [[confluence_get_space_permissions_assignments]] — `GET /spaces/{id}/permissions` — Get space permissions assignments
- [[confluence_get_available_space_permissions]] — `GET /space-permissions` — Get available space permissions

## Space Permission Transition

- [[confluence_list_unassigned_space_permission_combinations]] — `GET /space-permissions/transition/combinations` — List unassigned space permission combinations
- [[confluence_generate_space_permission_combinations]] — `POST /space-permissions/transition/combinations` — Generate space permission combinations ✏️
- [[confluence_bulk_assign_space_permission_roles]] — `POST /space-permissions/transition/role-assignments` — Bulk assign space permission roles ✏️
- [[confluence_bulk_remove_space_permission_access]] — `POST /space-permissions/transition/access-removals` — Bulk remove space permission access ✏️
- [[confluence_get_space_permission_transition_task_status]] — `GET /space-permissions/transition/tasks/{taskId}` — Get space permission transition task status

## Space Properties

- [[confluence_get_space_properties_in_space]] — `GET /spaces/{space-id}/properties` — Get space properties in space
- [[confluence_create_space_property_in_space]] — `POST /spaces/{space-id}/properties` — Create space property in space ✏️
- [[confluence_get_space_property_by_id]] — `GET /spaces/{space-id}/properties/{property-id}` — Get space property by id
- [[confluence_update_space_property_by_id]] — `PUT /spaces/{space-id}/properties/{property-id}` — Update space property by id ✏️
- [[confluence_delete_space_property_by_id]] — `DELETE /spaces/{space-id}/properties/{property-id}` — Delete space property by id ✏️

## Space Roles

- [[confluence_get_available_space_roles]] — `GET /space-roles` — Get available space roles
- [[confluence_create_a_space_role]] — `POST /space-roles` — Create a space role ✏️
- [[confluence_get_space_role_by_id]] — `GET /space-roles/{id}` — Get space role by ID
- [[confluence_update_a_space_role]] — `PUT /space-roles/{id}` — Update a space role ✏️
- [[confluence_delete_a_space_role]] — `DELETE /space-roles/{id}` — Delete a space role ✏️
- [[confluence_get_space_role_mode]] — `GET /space-role-mode` — Get space role mode
- [[confluence_get_space_role_assignments]] — `GET /spaces/{id}/role-assignments` — Get space role assignments
- [[confluence_set_space_role_assignments]] — `POST /spaces/{id}/role-assignments` — Set space role assignments ✏️

## Task

- [[confluence_get_tasks]] — `GET /tasks` — Get tasks
- [[confluence_get_task_by_id]] — `GET /tasks/{id}` — Get task by id
- [[confluence_update_task]] — `PUT /tasks/{id}` — Update task ✏️

## User

- [[confluence_create_bulk_user_lookup_using_ids]] — `POST /users-bulk` — Create bulk user lookup using ids ✏️
- [[confluence_check_site_access_for_a_list_of_emails]] — `POST /user/access/check-access-by-email` — Check site access for a list of emails
- [[confluence_invite_a_list_of_emails_to_the_site]] — `POST /user/access/invite-by-email` — Invite a list of emails to the site ✏️

## Version

- [[confluence_get_attachment_versions]] — `GET /attachments/{id}/versions` — Get attachment versions
- [[confluence_get_version_details_for_attachment_version]] — `GET /attachments/{attachment-id}/versions/{version-number}` — Get version details for attachment version
- [[confluence_get_blog_post_versions]] — `GET /blogposts/{id}/versions` — Get blog post versions
- [[confluence_get_version_details_for_blog_post_version]] — `GET /blogposts/{blogpost-id}/versions/{version-number}` — Get version details for blog post version
- [[confluence_get_page_versions]] — `GET /pages/{id}/versions` — Get page versions
- [[confluence_get_version_details_for_page_version]] — `GET /pages/{page-id}/versions/{version-number}` — Get version details for page version
- [[confluence_get_custom_content_versions]] — `GET /custom-content/{custom-content-id}/versions` — Get custom content versions
- [[confluence_get_version_details_for_custom_content_version]] — `GET /custom-content/{custom-content-id}/versions/{version-number}` — Get version details for custom content version
- [[confluence_get_footer_comment_versions]] — `GET /footer-comments/{id}/versions` — Get footer comment versions
- [[confluence_get_version_details_for_footer_comment_version]] — `GET /footer-comments/{id}/versions/{version-number}` — Get version details for footer comment version
- [[confluence_get_inline_comment_versions]] — `GET /inline-comments/{id}/versions` — Get inline comment versions
- [[confluence_get_version_details_for_inline_comment_version]] — `GET /inline-comments/{id}/versions/{version-number}` — Get version details for inline comment version

## Whiteboard

- [[confluence_create_whiteboard]] — `POST /whiteboards` — Create whiteboard ✏️
- [[confluence_get_whiteboard_by_id]] — `GET /whiteboards/{id}` — Get whiteboard by id
- [[confluence_delete_whiteboard]] — `DELETE /whiteboards/{id}` — Delete whiteboard ✏️
