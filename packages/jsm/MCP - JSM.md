---
tags:
  - moc
  - mcp
  - api/app/jsm
up: "[[MCP Tools]]"
---
# MCP - JSM

- **Tools:** 73 (exposed: 6; the others via `run_vault_tool`)
- **Requests only:** 1
- **Instance:** `instance` parameter — notes tagged `atlassian/instance`
- **Official documentation:** https://developer.atlassian.com/cloud/jira/service-desk/rest/

Legend: ✏️ writes data · 🔒 restricted (Connect/Forge app or OAuth) · 📎 multipart/binary · ⭐ exposed in the client tool list.

## Assets

- [[jsm_get_assets_workspaces]] — `GET /rest/servicedeskapi/assets/workspace` — Get assets workspaces ⭐

## Customer

- [[jsm_create_customer]] — `POST /rest/servicedeskapi/customer` — Create customer ✏️
- [[jsm_revoke_portal_only_access_for_user]] — `PUT /rest/servicedeskapi/customer/user/{accountId}/revoke-portal-only-access` — Revoke portal only access for user ✏️

## Info

- [[jsm_get_info]] — `GET /rest/servicedeskapi/info` — Get info

## Knowledgebase

- [[jsm_get_articles]] — `GET /rest/servicedeskapi/knowledgebase/article` — Get articles

## Organization

- [[jsm_get_organizations]] — `GET /rest/servicedeskapi/organization` — Get organizations
- [[jsm_create_organization]] — `POST /rest/servicedeskapi/organization` — Create organization ✏️
- [[jsm_get_organization]] — `GET /rest/servicedeskapi/organization/{organizationId}` — Get organization
- [[jsm_delete_organization]] — `DELETE /rest/servicedeskapi/organization/{organizationId}` — Delete organization ✏️
- [[jsm_get_properties_keys]] — `GET /rest/servicedeskapi/organization/{organizationId}/property` — Get properties keys
- [[jsm_get_property]] — `GET /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}` — Get property
- [[jsm_set_property]] — `PUT /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}` — Set property ✏️
- [[jsm_delete_property]] — `DELETE /rest/servicedeskapi/organization/{organizationId}/property/{propertyKey}` — Delete property ✏️
- [[jsm_get_users_in_organization]] — `GET /rest/servicedeskapi/organization/{organizationId}/user` — Get users in organization
- [[jsm_add_users_to_organization]] — `POST /rest/servicedeskapi/organization/{organizationId}/user` — Add users to organization ✏️
- [[jsm_remove_users_from_organization]] — `DELETE /rest/servicedeskapi/organization/{organizationId}/user` — Remove users from organization ✏️
- [[jsm_get_organizations_get]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization` — Get organizations
- [[jsm_add_organization]] — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization` — Add organization ✏️
- [[jsm_remove_organization]] — `DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/organization` — Remove organization ✏️

## Request

- [[jsm_get_customer_requests]] — `GET /rest/servicedeskapi/request` — Get customer requests ⭐
- [[jsm_create_customer_request]] — `POST /rest/servicedeskapi/request` — Create customer request ✏️⭐
- [[jsm_validate_customer_request]] — `POST /rest/servicedeskapi/request/validate` — Validate customer request
- [[jsm_get_customer_request_by_id_or_key]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}` — Get customer request by id or key
- [[jsm_get_approvals]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/approval` — Get approvals
- [[jsm_get_approval_by_id]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}` — Get approval by id
- [[jsm_answer_approval]] — `POST /rest/servicedeskapi/request/{issueIdOrKey}/approval/{approvalId}` — Answer approval ✏️
- [[jsm_get_attachments_for_request]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment` — Get attachments for request
- [[jsm_create_comment_with_attachment]] — `POST /rest/servicedeskapi/request/{issueIdOrKey}/attachment` — Create comment with attachment ✏️
- [[jsm_get_attachment_content]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId}` — Get attachment content
- [[jsm_get_attachment_thumbnail]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/attachment/{attachmentId}/thumbnail` — Get attachment thumbnail
- [[jsm_get_request_comments]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/comment` — Get request comments ⭐
- [[jsm_create_request_comment]] — `POST /rest/servicedeskapi/request/{issueIdOrKey}/comment` — Create request comment ✏️
- [[jsm_get_request_comment_by_id]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}` — Get request comment by id
- [[jsm_get_comment_attachments]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/comment/{commentId}/attachment` — Get comment attachments
- [[jsm_get_subscription_status]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/notification` — Get subscription status
- [[jsm_subscribe]] — `PUT /rest/servicedeskapi/request/{issueIdOrKey}/notification` — Subscribe ✏️
- [[jsm_unsubscribe]] — `DELETE /rest/servicedeskapi/request/{issueIdOrKey}/notification` — Unsubscribe ✏️
- [[jsm_get_request_participants]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/participant` — Get request participants
- [[jsm_add_request_participants]] — `POST /rest/servicedeskapi/request/{issueIdOrKey}/participant` — Add request participants ✏️
- [[jsm_remove_request_participants]] — `DELETE /rest/servicedeskapi/request/{issueIdOrKey}/participant` — Remove request participants ✏️
- [[jsm_get_sla_information]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/sla` — Get sla information
- [[jsm_get_sla_information_by_id]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/sla/{slaMetricId}` — Get sla information by id
- [[jsm_get_customer_request_status]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/status` — Get customer request status
- [[jsm_get_customer_transitions]] — `GET /rest/servicedeskapi/request/{issueIdOrKey}/transition` — Get customer transitions
- [[jsm_perform_customer_transition]] — `POST /rest/servicedeskapi/request/{issueIdOrKey}/transition` — Perform customer transition ✏️
- [[jsm_get_feedback]] — `GET /rest/servicedeskapi/request/{requestIdOrKey}/feedback` — Get feedback
- [[jsm_post_feedback]] — `POST /rest/servicedeskapi/request/{requestIdOrKey}/feedback` — Post feedback ✏️
- [[jsm_delete_feedback]] — `DELETE /rest/servicedeskapi/request/{requestIdOrKey}/feedback` — Delete feedback ✏️

## Requesttype

- [[jsm_get_all_request_types]] — `GET /rest/servicedeskapi/requesttype` — Get all request types

## Servicedesk

- [[jsm_get_service_desks]] — `GET /rest/servicedeskapi/servicedesk` — Get service desks ⭐
- [[jsm_get_service_desk_by_id]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}` — Get service desk by id
- [[JSM - Attach temporary file]] — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/attachTemporaryFile` — Attach temporary file ✏️📎
- [[jsm_get_customers]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer` — Get customers
- [[jsm_add_customers]] — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer` — Add customers ✏️
- [[jsm_remove_customers]] — `DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer` — Remove customers ✏️
- [[jsm_invite_customer]] — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/invite` — Invite customer ✏️
- [[jsm_get_articles_get]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/knowledgebase/article` — Get articles
- [[jsm_get_queues]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue` — Get queues
- [[jsm_get_queue]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}` — Get queue
- [[jsm_get_issues_in_queue]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/queue/{queueId}/issue` — Get issues in queue
- [[jsm_get_request_types]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype` — Get request types ⭐
- [[jsm_create_request_type]] — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype` — Create request type ✏️
- [[jsm_check_request_type_permissions]] — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/permissions/check` — Check request type permissions
- [[jsm_get_request_type_by_id]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}` — Get request type by id
- [[jsm_delete_request_type]] — `DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}` — Delete request type ✏️
- [[jsm_get_request_type_fields]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/field` — Get request type fields
- [[jsm_get_properties_keys_get]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property` — Get properties keys
- [[jsm_get_property_get]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}` — Get property
- [[jsm_set_property_put]] — `PUT /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}` — Set property ✏️
- [[jsm_delete_property_delete]] — `DELETE /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype/{requestTypeId}/property/{propertyKey}` — Delete property ✏️
- [[jsm_get_request_type_groups]] — `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttypegroup` — Get request type groups

## Other operations

- [[jsm_create_customer_post]] — `POST /rest/servicedeskapi/customer/skip-permission-check` — Create customer ✏️
- [[jsm_view_knowledge_base_article]] — `GET /rest/servicedeskapi/knowledgebase/article/view/{pageId}` — View knowledge base article
- [[jsm_add_customers_post]] — `POST /rest/servicedeskapi/servicedesk/{serviceDeskId}/customer/skip-permission-check` — Add customers ✏️
