#debuginfo not supported with Go
%global debug_package %{nil}

%global gopath      %{_datadir}/gocode
%global import_path github.com/openshift/oc
%global golang_version 1.10

%global commit 074039a0a9c137967fba3e667b9849d60e5054d8
%global sversion %{version}

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
%setup -q -n oc-%{commit}

%build
echo "GOLANG DEBUG OUTPUT"
go version
mkdir -p $HOME/go
mkdir -p $HOME/go/{bin,pkg,src}
export GOPATH=$HOME/go
export GOBIN=$(go env GOPATH)/bin
export PATH=$PATH:$GOPATH
export PATH=$PATH:$GOBIN
make oc

%install
PLATFORM="$(go env GOHOSTOS)/$(go env GOHOSTARCH)"
install -d %{buildroot}%{_bindir}
# Install linux components
bin=oc 
echo "+++ INSTALLING ${bin}"
install -p -m 755 ${bin} %{buildroot}%{_bindir}/${bin}

%files
%{_bindir}/oc


%changelog
* Sun Oct 18 2020 JJ Asghar <jjasghar@gmail.com> 4.6
- Initial version of the package
