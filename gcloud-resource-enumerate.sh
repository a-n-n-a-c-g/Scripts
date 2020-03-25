#! /bin/bash

# https://googleapis.dev/python/cloudresourcemanager/latest/index.html
# https://cloud.google.com/resource-manager/reference/rest/v1/projects/list
# https://medium.com/google-cloud/using-gcloud-and-python-client-library-with-google-compute-engine-eaf1b19d8099
# https://cloud.google.com/resource-manager/docs/listing-all-resources
# https://cloud.google.com/sdk/gcloud/reference/projects/list

gcloud projects list --format 'value(project_id)' --sort-by=project_id > projects.txt

current_dir=`pwd`
projects="$current_dir/projects.txt"

while IFS= read -r line
do
    echo -e "\nRUNNING ON $line" #TODO: make this count how many lines are left
    

    #look for functions
    func_project=`yes N | gcloud functions list --format 'value(name)' --project $line --quiet --verbosity="none"`
    if [[ $func_project ]]; then
        echo "functions: $func_project"
    else
        echo 'no functions'
    fi

    #look for app instances
    app_project=`yes N | gcloud app describe --format 'value(name)' --project $line --quiet --verbosity="none"`
    if [[ $app_project ]]; then
        echo "apps: $app_project"

        #look for app firewalls
        app_firewall=`gcloud app firewall-rules list --project $line --format="text" --quiet --verbosity="none"`
        if [[ $app_firewall ]]; then
            echo "app firewall: $app_firewall"
        else
            echo 'no firewall on the app'
        fi

    else
        echo 'no apps'
    fi

    #look for compute instances
    compute_insts_project=`yes N | gcloud compute instances list --format 'value(name)' --project $line --quiet --verbosity="none"`
    if [[ $compute_insts_project ]]; then
        echo "compute instances: $compute_insts_project"
    else
        echo 'no compute instances'
    fi

    #look for compute firewall-rules
    compute_firewall=`yes N | gcloud compute firewall-rules list --format="text" --project $line --quiet --verbosity="none"`
     if [[ $compute_firewall ]]; then
         echo "compute firewall rules: $compute_firewall"
     else
         echo 'no firewall rules'
     fi

    #look for compute forwarding-rules
    compute_forwarding=`yes N | gcloud compute forwarding-rules list --format="text" --project $line --quiet --verbosity="none"`
    if [[ $compute_forwarding ]]; then
        echo "compute forwarding rules: $compute_forwarding"
    else
        echo 'no forwarding rules'
    fi

    #look for compute security-policies
    compute_security=`yes N | gcloud compute security-policies list --format="text" --project $line --quiet --verbosity="none"`
    if [[ $compute_security ]]; then
       echo "compute security policies: $compute_security"
    else
        echo 'no compute security policies'
    fi

    #look for compute ssl-certificates
    comp_ssl=`yes N | gcloud compute ssl-certificates list --format="text" --project $line --quiet --verbosity="none"`
    if [[ $comp_ssl ]]; then
        echo "ssl certificates: $comp_ssl"
    else
        echo 'no ssl certificates'
    fi

    #look for compute vpn-gateways
    comp_vpn_gw=`yes N | gcloud compute vpn-gateways list --format="text" --project $line --quiet --verbosity="none"`
    if [[ $comp_vpn_gw ]]; then
        echo "compute vpn-gateways: $comp_vpn_gw"
    else
        echo 'no compute vpn-gateways'
    fi

    #look for compute vpn-tunnels
    comp_vpn_tunnels=`yes N | gcloud compute vpn-tunnels list --format="text" --project $line --quiet --verbosity="none"`
    if [[ $comp_vpn_tunnels ]]; then
        echo "compute vpn-tunnels: $comp_vpn_tunnels"
    else
        echo 'no compute vpn-tunnels'
    fi

    #look for container clusters
    cont_cluster=`yes N | gcloud container clusters list --format 'value(name)' --project $line --quiet --verbosity="none"`
    if [[ $cont_cluster ]]; then
        echo "container clusters: $cont_cluster"
    else
        echo 'no container clusters'
    fi

    # #TODO: look for cloud billing
    # app_project=`yes N | gcloud  app describe --format 'value(name)' --project $line --quiet --verbosity="none"`
    # if [[ $app_project ]]; then
        # echo $app_project
    # else
        # echo 'no apps'
    # fi

    # #TODO: look for usage
    # app_project=`yes N | gcloud  app describe --format 'value(name)' --project $line --quiet --verbosity="none"`
    # if [[ $app_project ]]; then
        # echo $app_project
    # else
        # echo 'no apps'
    # fi
done <"$projects"
