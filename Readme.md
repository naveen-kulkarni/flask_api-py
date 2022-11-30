==============================================================================================
Prerequisites
==============================================================================================
	Python:
		Python > 3.8
		Pip install pysqlite3 (if python < 3.8, sqlite3 comes as default if >3.9 )
		pip install flask

	Docker:
		Version : 20.10.
	
	Kubernetes:
		Version : 1.25

==============================================================================================
Docker
==============================================================================================

Docker Image is created and it can be pulled from below docker hub.
	$docker pull naveenvk888/flask-api-db:db_api_flask

To List the docker image.
	$docker images

To create a container from the image.
	$docker run --name <Container-Name-of-ours> -p 5000:5000 <Image-ID>
	
To Start a container
	List the container
		$docker ps -a
	Start the container
		$docker start <Container-ID>

To get into container
	$docker exec -it <Container-ID> /bin/sh
	
==============================================================================================
Kubernetes - Helm Chart Way of Deployments
==============================================================================================
Clone the helm-chart from the github account.
	$git clone https://github.com/naveen-kulkarni/flask_api-py/tree/main/Helm%20Chart/city

Run the helm-chart
	$helm install <Deployment-Name> city 

To list helm chart.
        $helm list

To delete helm chart
        $helm remove <chart name>

Check the below commands to verify the deployments, pods and service
	$kubectl get deployments
	$kubectl get pods -o wide
	$kubectl get svc
	
To enter in to pod
	$kubectl exec -it <Pod-Name> -n <NameSpace> /bin/sh
==============================================================================================
Kubernetes Without helm-chart deployments
==============================================================================================
Clone the deployment.yaml file and service.yaml file from the git.

	$git clone https://github.com/naveen-kulkarni/flask_api-py/tree/main/kubernetes

Run the kubernets definition file 
	$kubectl create -f deployment.yaml
	$kubectl create -f service.yaml
	

Check the below commands to verify the deployments, pods and service
	$kubectl get deployments
	$kubectl get pods -o wide
	$kubectl get svc
	
To enter in to pod
	$kubectl exec -it <Pod-Name> -n <NameSpace> /bin/sh

==============================================================================================
Database
==============================================================================================
Name : Sqlite3
Library Name : pysqlite3

For checking the values of the tables in database

$sqlite3 <Database-Name>
.databases;
.tables;
.Select * from table name;
==============================================================================================
Others
==============================================================================================
GitHub Location : https://github.com/naveen-kulkarni/flask_api-py
Docker Hub image : naveenvk888/flask-api-db:db_api_flask

api.py - Flask based application.
db.py -  sqlite3 database creation.
Dockerfile - Dockerfile for image creation.
		$docker build --tag <Image-Name> .
Kubernetes : Contains the deployment.yaml and service.yaml file. A non-helm chart way of deployment.

Helm Chart/city : Contains a helm chart "city".
==============================================================================================

Should you have questions,don't hesitate to reach me on
naveenvk88@gmail.com.
