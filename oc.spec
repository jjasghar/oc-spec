#debuginfo not supported with Go
%global debug_package %{nil}

%global gopath      %{_datadir}/gocode
%global import_path github.com/openshift/client-go
%global golang_version 1.10

# Commit as of https://github.com/openshift/client-go/pull/162
%global commit 91d71ef2122c7b41d81ea07f7f5bff89daec755c
%global sversion %{version}

# os_git_vars needed to run hack scripts during rpm builds
# place to look for the kube, catalog and etcd commit hashes are the lock files in the origin tree, seems that origin build scripts are ignorant about what origin is bundling...
%{!?os_git_vars:
%global os_git_vars OS_GIT_COMMIT=%{shortcommit} OS_GIT_VERSION=v3.11.0+%{shortcommit} OS_GIT_MAJOR=3 OS_GIT_MINOR=11+ OS_GIT_PATCH=0 OS_GIT_TREE_STATE=clean KUBE_GIT_VERSION=v1.10.0+%{kube_shortcommit} KUBE_GIT_MAJOR=1 KUBE_GIT_MINOR=10+ KUBE_GIT_COMMIT=%{kube_shortcommit} ETCD_GIT_COMMIT=%{etcd_shortcommit} ETCD_GIT_VERSION=v3.2.16-0-%{etcd_shortcommit} OS_GIT_CATALOG_VERSION=v0.1.9}

Name:           oc
Version:        4.6
Release:        1%{?dist}
Summary:        origin-cli to interface with OpenShift Clusters

License:       Apache-v2
URL:           https://%{import_path}
Source0:       https://%{import_path}/archive/%{commit}/%{name}-%{sversion}.tar.gz


%description
With OpenShift Client CLI (oc), you can create applications and manage OpenShift resources. 
It is built on top of kubectl which means it provides its full capabilities to connect 
with any kubernetes compliant cluster, and on top adds commands simplifying interaction 
with an OpenShift cluster.

%prep
%setup -q -n client-go-%{commit}

%build
echo "GOLANG DEBUG OUTPUT"
go version
mkdir -p $HOME/go
mkdir -p $HOME/go/{bin,pkg,src}
export GOPATH=$HOME/go
export GOBIN=$(go env GOPATH)/bin
export PATH=$PATH:$GOPATH
export PATH=$PATH:$GOBIN
echo "package:" > glide.yaml
echo "import:" >> glide.yaml
echo "- package: github.com/openshift/client-go" >> glide.yaml
glide up -v

%install
PLATFORM="$(go env GOHOSTOS)/$(go env GOHOSTARCH)"
install -d %{buildroot}%{_bindir}
# Install linux components
bin=oc 
echo "+++ INSTALLING ${bin}"
install -p -m 755 _output/local/bin/${PLATFORM}/${bin} %{buildroot}%{_bindir}/${bin}

%files
%{_bindir}/oc


%changelog
* Sun Oct 18 2020 JJ Asghar <jjasghar@gmail.com> 4.6
- Initial version of the package
