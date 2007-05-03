#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	DKIM
Summary:	Mail::DKIM - Signs/verifies Internet mail with DKIM/DomainKey signatures
#Summary(pl.UTF-8):
Name:		perl-Mail-DKIM
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mail/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9d50bc57eeb41d36b9ccc1cb72a64e9a
URL:		http://search.cpan.org/dist/Mail-DKIM/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl-Crypt-OpenSSL-RSA >= 0.22
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Error
BuildRequires:	perl-MailTools
BuildRequires:	perl-Net-DNS
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module is part of the dkimproxy program, located at
http://jason.long.name/dkimproxy/. I've tried to abstract out the DKIM
parts into this module, for use in other programs.

The Mail::DKIM module uses an object-oriented interface. You use one
of two different classes, depending on whether you are signing or
verifying a message. To sign, use the Mail::DKIM::Signer class. To
verify, use the Mail::DKIM::Verifier class. Simple, eh?

# %description -l pl.UTF-8
# TODO

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
