#! /bin/bash

check_for_errors () {
    if [[ $1 ]]; then
        echo $2: $1
    else
        echo "$2: none"
    fi
}

gcloud projects list --format 'value(project_id)' --sort-by=project_id > projects.txt

current_dir=`pwd`
projects="$current_dir/projects.txt"

while IFS= read -r line
do
    echo -e "\nPROJECT: $line"
    
    #look for functions
    func_project=`yes N | gcloud compute instances list --format 'value(name)' --project $line --quiet --verbosity="none"`
    check_for_errors "$func_project" "functions"

    #look for app instances
    app_project=`yes N | gcloud app describe --format 'value(name)' --project $line --quiet --verbosity="none"`
    check_for_errors "$app_project" "apps"

    #look for app firewalls
    app_firewall=`gcloud app firewall-rules list --project $line --format="text" --quiet --verbosity="none"`
    check_for_errors "$app_firewall" "app firewall rules"

    #look for compute instances
    compute_insts_project=`yes N | gcloud compute instances list --format 'value(name)' --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_insts_project" "compute instances"

    #look for compute firewall-rules
    compute_firewall=`yes N | gcloud compute firewall-rules list --format="text" --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_firewall" "compute firewall rules"

    #look for compute forwarding-rules
    compute_forwarding=`yes N | gcloud compute forwarding-rules list --format="text" --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_forwarding" "compute forwarding rules"

    #look for compute security-policies
    compute_security=`yes N | gcloud compute security-policies list --format="text" --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_security" "compute security policies"

    #look for compute ssl-certificates
    comp_ssl=`yes N | gcloud compute ssl-certificates list --format="text" --project $line --quiet --verbosity="none"`
    check_for_errors "$comp_ssl" "ssl certificates"

    #look for compute vpn-gateways
    comp_vpn_gw=`yes N | gcloud compute vpn-gateways list --format="text" --project $line --quiet --verbosity="none"`
    check_for_errors "$comp_vpn_gw" "vpn gateways"

    #look for compute vpn-tunnels
    comp_vpn_tunnels=`yes N | gcloud compute vpn-tunnels list --format="text" --project $line --quiet --verbosity="none"`
    check_for_errors "$comp_vpn_tunnels" "vpn tunnels"

    #look for container clusters
    cont_cluster=`yes N | gcloud container clusters list --format 'value(name)' --project $line --quiet --verbosity="none"`
    check_for_errors "$cont_cluster" "clusters"

    #TODO: look for cloud billing
    #TODO: look for usage

done <"$projects"
