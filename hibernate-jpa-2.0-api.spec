%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-jpa-2.0-api
Version:          1.0.1
Release:          15.2
Summary:          Java Persistence 2.0 (JSR 317) API
Group:		  Development/Java

License:          EPL and BSD
URL:              http://www.hibernate.org/

# svn export http://anonsvn.jboss.org/repos/hibernate/jpa-api/tags/hibernate-jpa-2.0-api-1.0.1.Final/ hibernate-jpa-2.0-api-1.0.1.Final
# tar -zcvf hibernate-jpa-2.0-api-1.0.1.Final.tar.gz hibernate-jpa-2.0-api-1.0.1.Final
Source0:          %{name}-%{namedversion}.tar.gz
Patch0:           %{name}-%{namedversion}-encoding.patch
Patch1:           %{name}-%{namedversion}-osgi-manifest.patch

BuildArch:        noarch

Requires:         java

BuildRequires:    java-devel
BuildRequires:    maven-local

BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin

%description
Hibernate definition of the Java Persistence 2.0 (JSR 317) API.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%patch1 -p1

%pom_xpath_remove pom:build/pom:extensions

%build
%mvn_build

%install
# Fixing wrong-file-end-of-line-encoding
sed -i 's/\r//' target/site/apidocs/jdstyle.css

%mvn_install

%files -f .mfiles
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.1-11
- Removed wagon extension

* Fri Feb 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.1-10
- Don't install depmap for javax.persistence:persistence-api

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Gerard Ryan <galileo@fedoraproject.org> 1.0.1-6
- Add OSGI info to MANIFEST.MF

* Fri Mar 16 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-5
- Relocated jars to _javadir
- Added javax.persistence:persistence-api POM mapping

* Sun Jan 15 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.1-4
- Fixed encoding

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-2
- Removed unnecessary macros, using new add_maven_depmap
- License fix

* Tue Jul 05 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Upstream release, license fix

* Fri May 20 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.0-1
- Initial packaging

