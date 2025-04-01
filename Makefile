SSH_KEY_PATH = .private/ssh_access.pem
EC2_USER = "ubuntu"
EC2_IP ?= $(EC2_SERVER_IP)

runlocal:
	python3 blog_heho/manage.py runserver

lint:
	pylint blog_heho/blog

startdocker: 
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

stopdocker:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

ssh:
	ssh -i "$(SSH_KEY_PATH)" $(EC2_USER)@$(EC2_IP)