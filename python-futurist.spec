%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name futurist

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        1%{?dist}
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
BuildRequires:  python-pbr
BuildRequires:  git
BuildRequires:  python-sphinx
BuildRequires:  python-openstackdocstheme
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
BuildRequires:  python3-monotonic
BuildRequires:  python3-prettytable
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
%autosetup -n %{pypi_name}-%{upstream_version} -S git

%build
%if 0%{?with_python3}
%py3_build
%endif # with_python3
%py2_build

# generate html docs
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


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

%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE

%changelog
* Wed Nov 22 2017 RDO <dev@lists.rdoproject.org> 1.3.1-1
- Update to 1.3.1

* Thu Aug 10 2017 Alfredo Moralejo <amoralej@redhat.com> 1.3.0-1
- Update to 1.3.0

