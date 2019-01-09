%if 0%{?fedora} || 0%{?rhel} > 7
%global with_python3 1
%endif

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
 
%package -n python2-%{pypi_name}
Summary:        Useful additions to futures, from the future
%{?python_provide:%python_provide python2-%{pypi_name}}
%if 0%{?fedora} < 23
Obsoletes:      python-futurist < %{version}-%{release}
%endif

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  git
BuildRequires:  python2-sphinx
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-prettytable
BuildRequires:  python2-setuptools
BuildRequires:  python2-six
%if 0%{?fedora} > 0 || 0%{?rhel} > 7
BuildRequires:  python2-futures
BuildRequires:  python2-monotonic
BuildRequires:  python2-contextlib2
%else
BuildRequires:  python-futures
BuildRequires:  python-monotonic
BuildRequires:  python-contextlib2
%endif

Requires:       python2-six >= 1.10.0
Requires:       python2-prettytable
%if 0%{?fedora} > 0 || 0%{?rhel} > 7
Requires:       python2-monotonic
Requires:       python2-futures >= 3.0
Requires:       python2-contextlib2 >= 0.4.0
%else
Requires:       python-monotonic
Requires:       python-futures >= 3.0
Requires:       python-contextlib2 >= 0.4.0
%endif

%description -n python2-%{pypi_name}
%{common_desc}

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Useful additions to futures, from the future
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-monotonic
BuildRequires:  python3-prettytable
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

Requires:       python3-six >= 1.10.0
Requires:       python3-monotonic
Requires:       python3-contextlib2 >= 0.4.0
Requires:       python3-prettytable

%description -n python3-%{pypi_name}
%{common_desc}
%endif

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Useful additions to futures, from the future - documentation

%description -n python-%{pypi_name}-doc
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
%if 0%{?with_python3}
%py3_build
%endif # with_python3
%py2_build

%if 0%{?with_doc}
# generate html docs
sphinx-build -W -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info
%endif

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
