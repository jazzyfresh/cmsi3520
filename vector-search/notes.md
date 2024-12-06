#! docker network inspect elastic
#! docker ps
#! docker logs container-id

#! docker exec
#! docker exec 8098613ccf55 bin/elasticsearch-create-enrollment-token --scope kibana
#! docker exec 942c6cb81a30 bin/kibana-verification-code


#! pbcopy < openAI.key
openssl s_client -connect localhost:9200 -servername localhost -showcerts </dev/null 2>/dev/null | openssl x509 -fingerprint -sha256 -noout -in /dev/stdin
