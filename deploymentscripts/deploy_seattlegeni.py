"""
<Program Name>
  deploy_clearinghouse.py

<Started>
  July 29, 2009

<Author>
  Justin Samuel

<Purpose>
  Deploys all components of clearinghouse. Some things (e.g. database setup,
  config file modification to enter db user/pass info, etc.) still need
  to be done after this is run. See the instructions at
  https://seattle.poly.edu/wiki/ClearinghouseInstallation

<Description>
  The script backs up the target deploy directory if it exists and the user
  wants to proceed. It then deploys all required files to the deploy
  directory the user specified.

<Usage>
  python deploy_clearinghouse.py <path/to/svn/trunk> <dir/to/deploy/to>
  
"""

import glob
import os
import shutil
import subprocess
import sys
import time





# This function was taken from preparetest. It seemed annoying to depend on
# preparetest just for this. If we use preparetest for anything else later on,
# (e.g. preparing tests?), then we should remove this.
def _copy_to_target(file_expr, target):
  """
  file_expr may contain wildcards
  target must specify an existing directory with no wildcards
  """
  files_to_copy = glob.glob(file_expr)
  for file_path in files_to_copy:
    if os.path.isfile(file_path):
      shutil.copyfile(file_path, target + "/" + os.path.basename(file_path))





def _print_post_deploy_instructions():
  print
  print "Deployed successfully. The file trunk/seattlegeni/README.txt contains the"
  print "rest of the info you'll need to get things running."





def main():
    
  if not len(sys.argv) == 3:
    exit_with_message(2, "Usage: python deploy_seattlegeni.py <path/to/svn/trunk> <dir/to/deploy/to>")
  
  trunkdir = sys.argv[1]
  deployroot = sys.argv[2]
  
  if not os.path.isdir(trunkdir):
    exit_with_message(1, "ERROR: the provided path to the svn trunk does not exist.")

  if not os.path.exists(os.path.join(trunkdir, "clearinghouse")):
    exit_with_message(1, "ERROR: the given svn trunk directory doesn't contains a seattlegeni directory.")

  # Warn the user if the provided deploy directory exists and if it should be replaced.
  # We actually rename rather than remove the old one, just to be paranoid.
  replace_deployment_dir = False
  if os.path.isdir(deployroot):
    print "WARNING: existing directory found at directory to deploy: " + deployroot
    ans = raw_input("Backup and replace this directory (copying config files to the new deployment)? [y/n]")
    replace_deployment_dir = str.lower(ans) == 'y'
    if not replace_deployment_dir:
      exit_with_message(2, "You chose not to replace the directory.")
    else:
      print
      renameddir = deployroot.rstrip('/').rstrip('\\') + '.bak.' + str(time.time())
      print "Renaming existing directory " + deployroot + " to " + renameddir
      shutil.move(deployroot, renameddir)

  # Create the directory we will deploy to.
  print "Creating directory " + deployroot
  os.mkdir(deployroot)

  # Copy over the clearinghouse files from svn to the deploy directory.
  #seattlegeni_svn = os.path.join(trunkdir, "seattlegeni", "website")
  clearinghouse_source_dir = os.path.join(trunkdir, "clearinghouse")
  clearinghouse_deploy_dir = os.path.join(deployroot, "clearinghouse")
  print "Copying " + clearinghouse_source_dir + " to " + clearinghouse_deploy_dir
  shutil.copytree(clearinghouse_source_dir, clearinghouse_deploy_dir, symlinks=True)

  # Inform the user to deploy the Repy runtime and library files in a 
  # directory called "seattle" for use within Clearinghouse code.
  # XXX In a future version of this script (and the other init/build scripts 
  # XXX that we happen to use), this user intervention won't be required.
  print "Don't forget to create a Repy runtime for the clearinghouse in "
  print "the directory " + clearinghouse_deploy_dir + "/seattle by calling "
  print "./clearinghouse/scripts/dist/build.py " + clearinghouse_deploy_dir + \ 
    "seattle"
  
  # If we replaced an existing directory, then copy the config files from the
  # old deployment to the new one.
  if replace_deployment_dir:
    # The website settings files.
    old_settings_path = os.path.join(renameddir, "clearinghouse", "website", "settings.py")
    new_settings_path = os.path.join(clearinghouse_deploy_dir, "website", "settings.py")
    print "Copying " + old_settings_path + " to " + new_settings_path
    # Use copy2 to preserve permissions, e.g. in case these weren't world-readable.
    shutil.copy2(old_settings_path, new_settings_path)
    
    # The keydb config file.
    old_keydb_config_path = os.path.join(renameddir, "clearinghouse", "keydb", "config.py")
    new_keydb_config_path = os.path.join(clearinghouse_deploy_dir, "keydb", "config.py")
    print "Copying " + old_keydb_config_path + " to " + new_keydb_config_path
    # Use copy2 to preserve permissions, e.g. in case these weren't world-readable.
    shutil.copy2(old_keydb_config_path, new_keydb_config_path)

    # The backend config file.
    old_keydb_config_path = os.path.join(renameddir, "clearinghouse", "backend", "config.py")
    new_keydb_config_path = os.path.join(clearinghouse_deploy_dir, "backend", "config.py")
    print "Copying " + old_keydb_config_path + " to " + new_keydb_config_path
    # Use copy2 to preserve permissions, e.g. in case these weren't world-readable.
    shutil.copy2(old_keydb_config_path, new_keydb_config_path)

  state_key_path = os.path.join(clearinghouse_deploy_dir, "node_state_transitions", "statekeys")
  beta_state_key_path = os.path.join(clearinghouse_deploy_dir, "node_state_transitions", "statekeys_beta")
  
  # Remove the production key from the deployment, as we don't want anyone to get confused by them.
  # If there is any error, just ignore it.
  try:
    shutil.rmtree(state_key_path, ignore_errors=True)
    shutil.rmtree(beta_state_key_path, ignore_errors=True)
  except:
    pass

  _print_post_deploy_instructions()





def exit_with_message(retval, message):
  print message
  print "Exiting."
  sys.exit(retval)





if __name__ == '__main__':
  main()
