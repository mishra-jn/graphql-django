import graphene

import ingredients.schema

class Query(ingredients.schema.Query, graphene.ObjectType):
	# This class will inherit from multiple queries
	# as we begin to add more apps to our projects
	pass

schema = graphene.Schema(query=Query)