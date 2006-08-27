Summary:	JBIG2 encoder
Summary(pl):	Koder JBIG2
Name:		jbig2enc
Version:	0.23
Release:	1
License:	Apache v2.0
Group:		Applications/Graphics
Source0:	http://www.imperialviolet.org/binary/%{name}-%{version}.tar.bz2
# Source0-md5:	30a9422b0abbcbc98000aa75135f8c39
Patch0:		%{name}-lept.patch
Patch1:		%{name}-shared.patch
URL:		http://www.imperialviolet.org/jbig2.html
BuildRequires:	leptonlib-devel >= 1.38
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
Requires:	leptonlib >= 1.38
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JBIG2 encoder.

%description -l pl
Koder JBIG2.

%package devel
Summary:	Development files for jbig2enc library
Summary(pl):	Pliki nagłówkowe dla biblioteki jbig2enc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	leptonlib-devel >= 1.38
Requires:	libstdc++-devel

%description devel
Development files for jbig2enc library.

%description devel -l pl
Pliki nagłówkowe dla biblioteki jbig2enc.

%package static
Summary:	Static version of jbig2enc library
Summary(pl):	Statyczna wersja biblioteki jbig2enc
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of jbig2enc library.

%description static -l pl
Statyczna wersja biblioteki jbig2enc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	EXTRA="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc PATENTS README jbig2enc.html
%attr(755,root,root) %{_bindir}/jbig2
%attr(755,root,root) %{_libdir}/libjbig2enc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjbig2enc.so
%{_libdir}/libjbig2enc.la
%{_includedir}/jbig2enc.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjbig2enc.a
