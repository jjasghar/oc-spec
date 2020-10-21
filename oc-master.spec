#debuginfo not supported with Go
%global debug_package %{nil}
%global goipath github.com/openshift/oc

%global gopath      %{_datadir}/gocode
%global import_path github.com/openshift/oc
%global golang_version 1.10

%global commit 657671383e03d9ef22c01fb7202fa44ce0a71e18
%global sversion %{version}
%global golicenses LICENCE

Name:           oc
Version:        master
Release:        1%{?dist}
Summary:        origin-cli to interface with OpenShift Clusters

License:       Apache-v2
URL:           https://%{import_path}
Source0:       https://%{import_path}/archive/%{commit}/%{name}-%{sversion}.tar.gz
BuildRequires: git,krb5-devel


%description
With OpenShift Client CLI (oc), you can create applications and manage OpenShift resources. 
It is built on top of kubectl which means it provides its full capabilities to connect 
with any kubernetes compliant cluster, and on top adds commands simplifying interaction 
with an OpenShift cluster.


%gopkg

%prep
%setup -q -n oc-%{commit}
%generate_buildrequires


%build
echo "GOLANG DEBUG OUTPUT"
go version
make GO_REQUIRED_MIN_VERSION:= oc

%install
install -p -m 0755 oc %{buildroot}%{_bindir}

%files
%{_bindir}/oc
%license %{golicenses}


%changelog
* Sun Oct 18 2020 JJ Asghar <jjasghar@gmail.com> 4.6
- Initial version of the package
