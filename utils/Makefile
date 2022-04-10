create-table:
	aws dynamodb create-table --cli-input-json file://create-menu-table.json
	aws dynamodb create-table --cli-input-json file://create-order-table.json
	aws dynamodb create-table --cli-input-json file://create-seating-table.json

populate-table:
	# aws dynamodb batch-write-item --request-items file://menu-table-items.json
	aws dynamodb batch-write-item --request-items file://seating-table-items.json
