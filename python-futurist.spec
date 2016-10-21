%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name futurist

Name:           python-%{pypi_name}
Version:        XXX
Release:        XXX
Summary:        Useful additions to futures, from the future

License:        ASL 2.0
URL:            http://docs.openstack.org/developer/futurist
Source0:        https://pypi.io/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
%package -n python2-%{pypi_name}
Summary:        Useful additions to futures, from the future
%{?python_provide:%python_provide python2-%{pypi_name}}
%if 0%{?fedora} < 23
Obsoletes:      python-futurist < %{version}-%{release}
%endif

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-futures
BuildRequires:  python-monotonic
BuildRequires:  python-prettytable
BuildRequires:  python-contextlib2
BuildRequires:  python-setuptools
BuildRequires:  python-six

Requires:       python-six >= 1.9.0
Requires:       python-monotonic
Requires:       python-futures >= 3.0
Requires:       python-contextlib2 >= 0.4.0
Requires:       python-prettytable

%description -n python2-%{pypi_name}
Code from the future, delivered to you in the now.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Useful additions to futures, from the future
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-oslo-sphinx
BuildRequires:  python3-monotonic
BuildRequires:  python3-prettytable
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

Requires:       python3-six >= 1.9.0
Requires:       python3-monotonic
Requires:       python3-contextlib2 >= 0.4.0
Requires:       python3-prettytable

%description -n python3-%{pypi_name}
Code from the future, delivered to you in the now.
%endif

%package -n python-%{pypi_name}-doc
Summary:        Useful additions to futures, from the future - documentation

%description -n python-%{pypi_name}-doc
Code from the future, delivered to you in the now. (documentation)

%description
========
Futurist
========

Code from the future, delivered to you in the now.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%if 0%{?with_python3}
%py3_build
%endif # with_python3
%py2_build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

%files -n python2-%{pypi_name}
%doc html README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-*-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc html README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-*-py?.?.egg-info
%endif

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
