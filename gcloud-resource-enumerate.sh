#! /bin/bash

check_for_errors () {
    if [[ $1 ]]; then
        echo \"$2\":$1,
        if [[ $3 ]]; then
            echo \"$4\":$3,
        fi
    else
        echo \"$2\":[],
    fi
}

gcloud projects list --format 'value(project_id)' --sort-by=project_id > projects.txt

current_dir=`pwd`
projects="$current_dir/projects.txt"


project_number=`cat $projects | wc -l | xargs`
>&2 echo -e "Found $project_number projects for processing\n"

project_counter=1

while IFS= read -r line
#line="weave-secops"
do
    
if [[ `gcloud alpha billing projects describe $line --format 'value(billingEnabled)'` = True ]]; then
    #echo True Billing

    >&2 echo -e "\nProcessing $line: Project $project_counter out of $project_number" 
    ((project_counter=project_counter+1))
    echo -e {\"project\":{
    echo \"name\":\"$line\",
    
    #look for functions
    func_project=`yes N | gcloud functions list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$func_project" "functions"

    #look for app instances and firewalls
    app_project=`yes N | gcloud app describe --format="json" --project $line --quiet --verbosity="none"`
    app_firewall=`gcloud app firewall-rules list --project $line --format="json" --quiet --verbosity="none"`
    check_for_errors "$app_project" "apps" "$app_firewall" "app firewall rules"

    #look for compute instances
    compute_insts_project=`yes N | gcloud compute instances list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_insts_project" "compute instances"

    #look for compute firewall-rules
    compute_firewall=`yes N | gcloud compute firewall-rules list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_firewall" "compute firewall rules"

    #look for compute forwarding-rules
    compute_forwarding=`yes N | gcloud compute forwarding-rules list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_forwarding" "compute forwarding rules"

    #look for compute security-policies
    compute_security=`yes N | gcloud compute security-policies list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$compute_security" "compute security policies"

    #look for compute ssl-certificates
    comp_ssl=`yes N | gcloud compute ssl-certificates list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$comp_ssl" "ssl certificates"

    #look for compute vpn-gateways
    comp_vpn_gw=`yes N | gcloud compute vpn-gateways list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$comp_vpn_gw" "vpn gateways"

    #look for compute vpn-tunnels
    comp_vpn_tunnels=`yes N | gcloud compute vpn-tunnels list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$comp_vpn_tunnels" "vpn tunnels"

    #look for container clusters
    cont_cluster=`yes N | gcloud container clusters list --format="json" --project $line --quiet --verbosity="none"`
    check_for_errors "$cont_cluster" "clusters"

    #TODO: look for cloud billing
    #TODO: look for usage

    echo \"scan date\":\"$(date)\"
    echo }}
>&2 echo "$line done"


else
    >&2 echo -e "\nNo billing setup; skipping project $project_counter ($line)."
    ((project_counter=project_counter+1))
fi


done <"$projects"
