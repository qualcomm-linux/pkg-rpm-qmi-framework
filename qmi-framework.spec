Name:           qmi-framework
Version:        0.1.4
Release:        1%{?dist}
Summary:        QMI Framework - Qualcomm Messaging Interface library

License:        BSD-3-Clause
URL:            https://github.com/qualcomm/qmi-framework
Source0:        https://github.com/qualcomm/qmi-framework/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig

%description
QMI Framework provides client and service-side libraries and sample utilities
for Qualcomm Messaging Interface (QMI) communication between applications and
remote subsystems.

%package -n libqcci1
Summary:        QMI Client Common Interface library
Requires:       libqencdec1%{?_isa} = %{version}-%{release}

%description -n libqcci1
QMI Framework provides the Client Common Interface (CCI) library for QMI
communication between applications and remote subsystems.

%package -n libqcsi1
Summary:        QMI Service Common Interface library
Requires:       libqencdec1%{?_isa} = %{version}-%{release}

%description -n libqcsi1
QMI Framework provides the Service Common Interface (CSI) library for QMI
communication between applications and remote subsystems.

%package -n libqencdec1
Summary:        QMI encoder and decoder library

%description -n libqencdec1
QMI Framework provides the encoder and decoder library for QMI message
encoding and decoding operations.

%package -n libqmi-common1
Summary:        QMI common support library

%description -n libqmi-common1
QMI Framework provides common functionality shared across QMI components
for communication between applications and remote subsystems.

%package devel
Summary:        Development files for %{name}
Requires:       libqcci1%{?_isa} = %{version}-%{release}
Requires:       libqcsi1%{?_isa} = %{version}-%{release}
Requires:       libqencdec1%{?_isa} = %{version}-%{release}
Requires:       libqmi-common1%{?_isa} = %{version}-%{release}

%description devel
Development headers and pkg-config files for building applications against
QMI Framework.

%package utils
Summary:        Test binaries for %{name}
Requires:       libqcci1%{?_isa} = %{version}-%{release}
Requires:       libqcsi1%{?_isa} = %{version}-%{release}
Requires:       libqencdec1%{?_isa} = %{version}-%{release}
Requires:       libqmi-common1%{?_isa} = %{version}-%{release}

%description utils
Test programs (qcci_test, qcsi_test) for QMI Framework.

%prep
%autosetup

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license LICENSE
%doc README.md CODE-OF-CONDUCT.md CONTRIBUTING.md

%files -n libqcci1
%{_libdir}/libqcci.so.1*

%files -n libqcsi1
%{_libdir}/libqcsi.so.1*

%files -n libqencdec1
%{_libdir}/libqencdec.so.1*

%files -n libqmi-common1
%{_libdir}/libqmi_common.so.1*

%files devel
%{_includedir}/qmi_framework/
%{_libdir}/libqcci.so
%{_libdir}/libqcsi.so
%{_libdir}/libqencdec.so
%{_libdir}/libqmi_common.so
%{_libdir}/pkgconfig/qmi-framework.pc

%files utils
%{_bindir}/qcci_test
%{_bindir}/qcsi_test

%changelog
* Wed Aug 13 2026 Vishnu Santhosh <vishnu.santhosh@oss.qualcomm.com> - 0.1.4-1
- Initial RPM packaging for qmi-framework 0.1.4
