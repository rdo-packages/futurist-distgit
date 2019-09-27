# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name futurist

%global common_desc \
Code from the future, delivered to you in the now.

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Useful additions to futures, from the future

License:        ASL 2.0
URL:            http://docs.openstack.org/developer/futurist
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

%package -n python%{pyver}-%{pypi_name}
Summary:        Useful additions to futures, from the future
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}}
%if 0%{?fedora} < 23
Obsoletes:      python-futurist < %{version}-%{release}
%endif
%if %{pyver} == 3
Obsoletes:      python2-%{pypi_name} < %{version}-%{release}
%endif

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  git
BuildRequires:  python%{pyver}-prettytable
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  python%{pyver}-six
BuildRequires:  python%{pyver}-monotonic
BuildRequires:  python%{pyver}-contextlib2
# Handle python2 exception
%if %{pyver} == 2
BuildRequires:  python%{pyver}-futures
%endif

Requires:       python%{pyver}-six >= 1.10.0
Requires:       python%{pyver}-prettytable
Requires:       python%{pyver}-monotonic
Requires:       python%{pyver}-contextlib2 >= 0.4.0
# Handle python2 exception
%if %{pyver} == 2
Requires:       python%{pyver}-futures >= 3.0
%endif

%description -n python%{pyver}-%{pypi_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python%{pyver}-%{pypi_name}-doc
Summary:        Useful additions to futures, from the future - documentation
%{?python_provide:%python_provide python%{pyver}-%{pypi_name}-doc}
%if %{pyver} == 3
Obsoletes:      python2-%{pypi_name}-doc < %{version}-%{release}
%endif

BuildRequires:  python%{pyver}-sphinx
BuildRequires:  python%{pyver}-openstackdocstheme

%description -n python%{pyver}-%{pypi_name}-doc
%{common_desc}
%endif

%description
========
Futurist
========

%{common_desc}

%prep
%autosetup -n %{pypi_name}-%{upstream_version} -S git

%build
%{pyver_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-%{pyver} -W -b html doc/source doc/build/html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%{pyver_install}

%files -n python%{pyver}-%{pypi_name}
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{pypi_name}
%{pyver_sitelib}/%{pypi_name}-*-py?.?.egg-info

%if 0%{?with_doc}
%files -n python%{pyver}-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
