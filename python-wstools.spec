#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	WSDL parsing services package for Web Services for Python 2
Summary(pl.UTF-8):	Pakiet usług analizy WSDL dla usług WWW dla Pythona 2
Name:		python-wstools
Version:	0.4.8
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/wstools/
Source0:	https://files.pythonhosted.org/packages/source/w/wstools/wstools-%{version}.tar.gz
# Source0-md5:	bf01cc513bf109950bfa426dedeffa06
URL:		https://pypi.org/project/wstools/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 1.10
BuildRequires:	python-pytest-runner
BuildRequires:	python-setuptools >= 1:17.1
%if %{with tests}
BuildRequires:	python-py >= 1.4
BuildRequires:	python-pytest >= 2.9.1
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-pbr >= 1.10
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-setuptools >= 1:17.1
%if %{with tests}
BuildRequires:	python3-py >= 1.4
BuildRequires:	python3-pytest >= 2.9.1
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WSDL parsing services package for Web Services for Python.

%description -l pl.UTF-8
Pakiet usług analizy WSDL dla usług WWW (Web Services) dla Pythona.

%package -n python3-wstools
Summary:	WSDL parsing services package for Web Services for Python 3
Summary(pl.UTF-8):	Pakiet usług analizy WSDL dla usług WWW dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-wstools
WSDL parsing services package for Web Services for Python.

%description -n python3-wstools -l pl.UTF-8
Pakiet usług analizy WSDL dla usług WWW (Web Services) dla Pythona.

%prep
%setup -q -n wstools-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt README.rst
%{py_sitescriptdir}/wstools
%{py_sitescriptdir}/wstools-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-wstools
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt README.rst
%{py3_sitescriptdir}/wstools
%{py3_sitescriptdir}/wstools-%{version}-py*.egg-info
%endif
