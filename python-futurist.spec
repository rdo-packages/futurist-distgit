%if 0%{?fedora}
%global with_python3 1
%endif

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global pypi_name futurist

Name:           python-%{pypi_name}
Version:        0.18.0
Release:        1%{?dist}
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
BuildRequires:  python-contextlib2
BuildRequires:  python-setuptools
BuildRequires:  python-six

Requires:       python-six >= 1.9.0
Requires:       python-monotonic
Requires:       python-futures >= 3.0
Requires:       python-contextlib2 >= 0.4.0

%description -n python2-%{pypi_name}
Code from the future, delivered to you in the now.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Useful additions to futures, from the future
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools
BuildRequires:  python3-six

Requires:       python3-six >= 1.9.0
Requires:       python3-monotonic
Requires:       python3-contextlib2 >= 0.4.0

%description -n python3-%{pypi_name}
Code from the future, delivered to you in the now.
%endif

%description
========
Futurist
========

Code from the future, delivered to you in the now.

%prep
%setup -qc -n %{pypi_name}-%{upstream_version}

mv %{pypi_name}-%{upstream_version} python2
pushd python2
# copy LICENSE etc. to top level dir
cp -a LICENSE ..
cp -a README.rst ..
popd

%if 0%{?with_python3}
cp -a python2 python3
%endif

%build
pushd python2
%{__python2} setup.py build
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
# Copy doc to top level dir
cp -a html ..
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py build
popd
%endif # with_python3

%install
pushd python2
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%if 0%{?with_python3}
pushd python3
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

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

%changelog
* Wed Sep 07 2016 Haikel Guemar <hguemar@fedoraproject.org> 0.18.0-1
- Update to 0.18.0

