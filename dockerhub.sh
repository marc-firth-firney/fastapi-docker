#!/bin/bash
# exit on first error
set -o errexit

# fetch current commit hash for tagging
HASH=$(git rev-parse --verify HEAD)

# specify project name for image tagging
PROJECTNAME="hammerson-tenant-data-service-fastapi"

# specify docker hub org name
ORGNAME="firneygroup"

# Blank array for capturing image urls
buildVar=( )

# list of containers in multistage build
declare -a arr=("tenant-api")

# loop through containers, build and tag
for i in "${arr[@]}"
do
   docker build --no-cache -t $ORGNAME/$PROJECTNAME-$i:$HASH -t $ORGNAME/$PROJECTNAME-$i:latest --target $i .
done

# push each container to the registry
for i in "${arr[@]}"
do
   # Push image to Docker registry
   docker push $ORGNAME/$PROJECTNAME-$i:$HASH
   docker push $ORGNAME/$PROJECTNAME-$i:latest

   # Store image url
   buildVar[${#buildVar[@]}]="$ORGNAME/$PROJECTNAME-$i:$HASH"
done

echo -e "\nBuild and push complete:\n"

# Iterate the loop to read and print each array element
for image in "${buildVar[@]}"
do
     echo -e "$image\n"
done
