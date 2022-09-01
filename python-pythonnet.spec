Name:           python-pythonnet
Version:        2.5.2
Release:        1
License:        MIT
Summary:        Net and Mono integration for Python
Url:            https://pythonnet.github.io/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pythonnet/pythonnet-%{version}.tar.gz
BuildRequires:  python3dist(setuptools)
BuildRequires:  fdupes
BuildRequires:  mono

%description
.Net and Mono integration for Python

%prep
%setup -q -n pythonnet-%{version}

%build
%py_build

%install
%py_install

%files
