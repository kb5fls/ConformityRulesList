from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


#project = 'projects/277941477175'
#project_list_command = "gcloud projects list --format json"
# 344560973671
# OAUTH_TOKEN=`gcloud auth print-access-token`
curl -X GET -H "Authorization: Bearer $OAUTH_TOKEN" -H "Content-Type: application/json" https://serviceusage.googleapis.com/v1/projects/344560973671/serv
ices/analytics.googleapis.com:enable