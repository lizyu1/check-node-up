require 'spec_helper'

describe package('sssd'), :if => os[:family] == 'redhat' do
  it { should be_installed }
end

describe port(636) do
  it { should be_listening.with('tcp') }
end

describe file('/etc/openldap/ldap.conf') do
  it { should be_owned_by 'root' }

describe command('ldaplist passwd abc') do
  its(:stdout) { should contain('abc') }
end