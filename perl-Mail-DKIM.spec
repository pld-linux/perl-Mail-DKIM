#
# Conditional build:
%bcond_with	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	DKIM
Summary:	Mail::DKIM - Signs/verifies Internet mail with DKIM/DomainKey signatures
Summary(pl.UTF-8):	Mail::DKIM - podpisywanie/sprawdzanie poczty przy użyciu podpisów DKIM/DomainKey
Name:		perl-Mail-DKIM
Version:	0.37
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f3e84ec6b5e42d4cbcc7c42ea2900649
URL:		http://search.cpan.org/dist/Mail-DKIM/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-OpenSSL-RSA >= 0.22
BuildRequires:	perl-Digest-SHA
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Error
BuildRequires:	perl-MailTools
BuildRequires:	perl-Net-DNS
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module is part of the dkimproxy program, located at
<http://jason.long.name/dkimproxy/>. I've tried to abstract out the
DKIM parts into this module, for use in other programs.

The Mail::DKIM module uses an object-oriented interface. You use one
of two different classes, depending on whether you are signing or
verifying a message. To sign, use the Mail::DKIM::Signer class. To
verify, use the Mail::DKIM::Verifier class. Simple, eh?

%description -l pl.UTF-8
Ten moduł Perla jest częścią programu dkimproxy, który można znaleźć
pod <http://jason.long.name/dkimproxy/>. Jest próbą wyodrębnienia
części DKIM do modułu w celu umożliwienia użycia przez inne programy.

Moduł Mail::DKIM wykorzystuje interfejs zorientowany obiektowo. Używa
się jednej z dwóch różnych klas w zależności od działania -
podpisywania lub sprawdzania podpisu wiadomości. Aby podpisać, należy
użyć klasy Mail::DKIM::Signer. Aby sprawdzić podpis, należy użyć klasy
Mail::DKIM::Verifier. Proste, prawda?

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Changes README TODO
%{perl_vendorlib}/Mail/*.pm
%{perl_vendorlib}/Mail/DKIM
%{_mandir}/man3/*
