set -e
homedir=$PWD
dir=`mktemp -d`
cd $dir
old=`cat $homedir/last_rev`
new=`LC_ALL=C svn info http://svn.opensuse.org/svn/zypp/trunk | grep ^Revision: | sed -e 's,.*: *,,'`
for pack in libsatsolver libzypp libzypp-testsuite-tools libzypp-bindings zypper; do
  
  case $pack in
    libsatsolver)
      repo=sat-solver
      ;;
    libzypp-testsuite-tools)
      repo=libzypp-testsuite
      ;;
    *)
      repo=$pack
  esac 

  url=http://svn.opensuse.org/svn/zypp/trunk/$repo
  log=`svn log -r$old:$new $url | grep ^r` || true
  test -n "$log" || continue

  osc co zypp:svn $pack
  cd zypp:svn/$pack

  svn cat $url/package/update_rpm | sh
  osc addremove
  osc ci
done
cd /
rm -rf $dir
echo $(($new+1)) > $homedir/last_rev
#svn ci -m "updated repo" $homedir/last_rev
