OSO = Oso.new
Relation = Oso::Polar::DataFiltering::Relation

OSO.register_class(
  User,
  fields: {
    email: String,
  }
)

OSO.register_class(
  Org,
  fields: {
    name: String,
    base_repo_role: String,
    billing_address: String,
    repos: Relation.new(
      kind: 'many',
      other_type: 'Repo',
      my_field: 'id',
      other_field: 'org_id',
    )
  }
)

OSO.register_class(
  Repo,
  fields: {
    name: String,
    org: Relation.new(
      kind: 'one',
      other_type: 'Org',
      my_field: 'org_id',
      other_field: 'id'
    ),
    issues: Relation.new(
      kind: 'many',
      other_type: 'Issue',
      my_field: 'id',
      other_field: 'repo_id'
    )
  }
)

OSO.register_class(
  Issue,
  fields: {
    title: String,
    repo: Relation.new(
      kind: 'one',
      other_type: 'Repo',
      my_field: 'repo_id',
      other_field: 'id'
    )
  }
)

OSO.register_class(
  OrgRole,
  fields: {
    name: String,
    org: Relation.new(
      kind: 'one',
      other_type: 'Org',
      my_field: 'org_id',
      other_field: 'id'
    ),
    user: Relation.new(
      kind: 'one',
      other_type: 'User',
      my_field: 'user_id',
      other_field: 'id'
    )
  }
)

OSO.register_class(
  RepoRole,
  fields: {
    name: String,
    repo: Relation.new(
      kind: 'one',
      other_type: 'Repo',
      my_field: 'repo_id',
      other_field: 'id'
    ),
    user: Relation.new(
      kind: 'one',
      other_type: 'User',
      my_field: 'user_id',
      other_field: 'id'
    )
  }
)

OSO.load_file("app/policy/authorization.polar")
OSO.enable_roles()
